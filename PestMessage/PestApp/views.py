import base64
import json
import random
import time

import itsdangerous
import requests
import rsa
import uuid
import datetime
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth import authenticate, hashers, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware import csrf
from django_redis import get_redis_connection
from dwebsocket.decorators import accept_websocket

from PestApp import models
from PestMessage import settings


# Create your views here.


class Token:
    @staticmethod
    def generate_token(user):
        salt = 'qwer'
        t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=3600)
        info = user
        res = t.dumps(info)
        token = res.decode()
        return token


def check_token(func):
    def wrapper(*args, **kwargs):
        token = args[0].headers['Authorization']
        salt = 'qwer'
        t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=3600)
        try:
            res = t.loads(token)
        except:
            return JsonResponse({'msg': '您的身份已经过期, 请重新登录'}, safe=False)
        return func(*args, **kwargs)

    return wrapper


class Captcha:
    @staticmethod
    @csrf_exempt
    def refresh_captcha(request):
        hashKey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashKey)
        return JsonResponse({'hashKey': hashKey, 'imageUrl': image_url}, safe=False)


def verify_captcha(func):
    def wrapper(*args, **kwargs):
        captcha = args[0].POST.get('captcha')
        captchaHashKey = args[0].POST.get('captchaHashKey')
        if captcha and captchaHashKey:
            try:
                get_captcha = CaptchaStore.objects.get(hashkey=captchaHashKey)
                if get_captcha.response == captcha.lower():
                    return func(*args, **kwargs)
                else:
                    return JsonResponse({'msg': '验证码有误'}, safe=False)
            except:
                return JsonResponse({'msg': '验证码有误'}, safe=False)
        else:
            return JsonResponse({'msg': '验证码有误'}, safe=False)

    return wrapper


@check_token
@login_required
def new_msg(request):
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=1581959283780'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    res = json.loads(res.text)
    totalData = res['data']['chinaTotal']['total']
    todayData = res['data']['chinaTotal']['today']
    cityData = {}
    dateTodayData = {}
    for i in range(10):
        temp = res['data']['chinaDayList'][len(res['data']['chinaDayList']) - i - 1]
        dateTodayData[temp['date']] = temp
    for i in range(34):
        temp = {
            'name': res['data']['areaTree'][2]['children'][i]['name'],
            'id': res['data']['areaTree'][2]['children'][i]['id'],
            'totalData': res['data']['areaTree'][2]['children'][i]['total'],
            'todayData': res['data']['areaTree'][2]['children'][i]['today'],
        }
        cityData[temp['name']] = temp
    response = {
        'todayData': todayData,
        'totalData': totalData,
        'cityData': cityData,
        'dateTodayData': dateTodayData,
    }
    return JsonResponse(response, safe=False)


class RetImg:
    @staticmethod
    @login_required
    def ret_img(request):
        imgId = request.GET.get('id')
        img = open('templates/Files/images/cover/img' + imgId + '.jpeg', 'rb')
        return HttpResponse(img.read(), content_type='image/bmp')


class Reply:

    @staticmethod
    @check_token
    @login_required
    def reply(request):
        if request.method == 'POST':
            conn = get_redis_connection()
            content = request.POST.get('content')
            commentsId = int(request.POST.get('commentsId'))
            date = datetime.datetime.now()
            keyWordsList = models.Keywords.objects.all().values_list()
            for item in keyWordsList:
                if item[1] in content:
                    return JsonResponse({'msg': '含有屏蔽关键字'}, safe=False)
            try:
                userId = request.user.id
                name = request.user.username
                models.Reply.objects.create(from_user_id=userId, to_comment_id=commentsId, date=date, content=content)
                response = {
                    'msg': '评论成功',
                    'name': name,
                }
                theUserId = models.Comments.objects.get(comment_id=commentsId).user_id
                conn.hincrby('Info:' + str(theUserId), 'NRep')
                return JsonResponse(response, safe=False)
            except:
                return JsonResponse({'msg': '你还没登录啊'}, safe=False)

        elif request.method == 'GET':
            commentsId = int(request.GET.get('commentsId'))
            ls = []
            try:
                result = models.Reply.objects.filter(to_comment_id=commentsId).values()
                for item in result:
                    userId = item['from_user_id']
                    item['date'] = str(item['date'])[:10]
                    item['from_name'] = models.UserInfoView.objects.get(user_id=userId).username
                    item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + models.UserInfoView.objects.get(
                        user_id=userId).username
                    ls.append(item)
                p = Paginator(ls, len(ls))
                pageNow = p.page(1).object_list
                return JsonResponse(pageNow, safe=False)
            except:
                return JsonResponse({'msg': '没有回复'}, safe=False)

        elif request.method == 'DELETE':
            replyId = int(request.GET.get('id'))
            models.Reply.objects.filter(reply_id=replyId).delete()
            return JsonResponse({'msg': '成功'}, safe=False)


class LikeAndDisLike:

    @staticmethod
    @check_token
    @login_required
    def inc_like_num(request):
        commentsId = int(request.POST.get('commentsId'))
        userId = request.user.id
        conn = get_redis_connection()
        if bytes(str(userId), encoding='utf-8') in conn.smembers('like:' + str(commentsId)):
            return JsonResponse({'msg': '你已经点过赞啦'}, safe=False)
        else:
            conn.sadd('like:' + str(commentsId), str(userId))
            likeNum = models.Comments.objects.get(comment_id=commentsId).likenum + 1
            models.Comments.objects.filter(comment_id=commentsId).update(likenum=likeNum)
            theUserId = models.Comments.objects.get(comment_id=commentsId).user_id
            conn.hincrby('Info:' + str(theUserId), 'LNum')
            conn.hincrby('Info:' + str(theUserId), 'NLike')
            return JsonResponse({'msg': '点赞成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def inc_dislike_num(request):
        commentsId = int(request.POST.get('commentsId'))
        userId = request.user.id
        conn = get_redis_connection()
        if bytes(str(userId), encoding='utf-8') in conn.smembers('DLike:' + str(commentsId)):
            return JsonResponse({'msg': '你已经点过踩啦'}, safe=False)
        else:
            conn.sadd('DLike:' + str(commentsId), str(userId))
            disLikeNum = models.Comments.objects.get(comment_id=commentsId).dislikenum + 1
            models.Comments.objects.filter(comment_id=commentsId).update(dislikenum=disLikeNum)
            theUserId = models.Comments.objects.get(comment_id=commentsId).user_id
            conn.hincrby('Info:' + str(theUserId), 'DLNum')
            conn.hincrby('Info:' + str(theUserId), 'NDLike')
            return JsonResponse({'msg': '点踩成功'}, safe=False)


class Comments:

    @staticmethod
    @check_token
    @login_required
    def personal_comments(request):
        if request.method == 'POST':
            conn = get_redis_connection()
            if request.POST.get('userId') is not None:
                userId = request.POST.get('userId')
            else:
                userId = request.user.id
            ls = []
            result = models.Comments.objects.filter(user_id=userId).values()
            for item in result:
                name = models.UserInfoView.objects.get(user_id=item['user_id']).username
                item['name'] = name
                item['reply'] = []
                item['date'] = str(item['date'])[:10]
                item['inputIsShow'] = False
                item['replyIsShow'] = False
                item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + name
                ls.append(item)
            p = Paginator(ls, 5)
            conn.hset('Info:' + str(userId), 'NRep', 0)
            conn.hset('Info:' + str(userId), 'NLike', 0)
            conn.hset('Info:' + str(userId), 'NDLike', 0)
            currentPage = request.POST.get('currentPage')
            if int(currentPage) > p.num_pages:
                return JsonResponse({'msg': '已经没有啦', 'pageCount': p.num_pages}, safe=False)
            else:
                pageNow = p.page(int(currentPage)).object_list
                return JsonResponse({'msg': '成功', 'pageCount': p.num_pages, 'pageNow': pageNow}, safe=False)

        elif request.method == 'DELETE':
            commentId = request.GET.get('commentId')
            try:
                models.Comments.objects.filter(comment_id=commentId).delete()
                models.Reply.objects.filter(to_comment_id=commentId).delete()
                return JsonResponse({'msg': '成功'}, safe=False)
            except:
                return JsonResponse({'msg': '删除失败'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def comments(request):
        if request.method == 'POST':
            field = request.POST.get('inputField')
            if field is not None:
                result = models.Comments.objects.all().values()
                ls = []
                for item in result:
                    item['date'] = str(item['date'])[:10]
                    if field in item['content']:
                        userId = item['user_id']
                        name = models.UserInfoView.objects.get(user_id=userId).username
                        item['name'] = name
                        item['reply'] = []
                        item['inputIsShow'] = False
                        item['replyIsShow'] = False
                        item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + name
                        ls.append(item)
                p = Paginator(ls, len(ls))
                pageNow = p.page(1).object_list
                response = {
                    'msg': '成功',
                    'pageNow': pageNow,
                }
                return JsonResponse(response, safe=False)
            else:
                value = request.POST.get('value')
                currentPage = request.POST.get('currentPage')
                ls = []
                result = models.Comments.objects.all().values()
                for item in result:
                    item['date'] = str(item['date'])[:10]
                    userId = item['user_id']
                    name = models.UserInfoView.objects.get(user_id=userId).username
                    item['name'] = name
                    item['reply'] = []
                    item['inputIsShow'] = False
                    item['replyIsShow'] = False
                    item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + name
                    ls.append(item)
                if value == 'true':
                    ls = sorted(ls, key=lambda ls: ls["likenum"], reverse=True)
                else:
                    ls.reverse()
                p = Paginator(ls, 10)
                if int(currentPage) > p.num_pages:
                    return JsonResponse({'msg': '已经没有啦', 'pageCount': p.num_pages}, safe=False)
                else:
                    pageNow = p.page(int(currentPage)).object_list
                    return JsonResponse(
                        {'msg': '成功', 'pageCount': p.num_pages, 'pageNow': pageNow,
                         'username': request.user.username},
                        safe=False)

    @staticmethod
    @check_token
    @login_required
    def writer_message(request):
        conn = get_redis_connection()
        myComments = request.POST.get('myComments')
        date = datetime.datetime.now()
        keyWordsList = models.Keywords.objects.all().values_list()
        for item in keyWordsList:
            if item[1] in myComments:
                return JsonResponse({'msg': '含有屏蔽关键字'}, safe=False)
        try:
            userId = request.user.id
            models.Comments.objects.create(user_id=userId, likenum=0, dislikenum=0, content=myComments,
                                           date=date)
            conn.hincrby('Info:' + str(userId), 'CNum')
            return JsonResponse({'msg': '发表成功'}, safe=False)
        except:
            return JsonResponse({'msg': '你还没登录啊'}, safe=False)


class Avatar:

    @staticmethod
    @login_required
    def people_ava(request, username):
        if request.method == 'GET':
            uid = models.UserInfo.objects.get(username=username).attachment_uuid
            if uid is None:
                img = open(settings.FILE_PATH + '9fb206a48683c9cc152534d3fe27bd95.jpeg', 'rb')
            else:
                attachment_name = models.Attachment.objects.get(attachment_uuid=uid).attachment_name
                img = open(settings.FILE_PATH + attachment_name, 'rb')
            return HttpResponse(img.read(), content_type='image/bmp')

    @staticmethod
    @login_required
    def vol_logo(request):
        img = open(settings.FILE_PATH + 'vounteerLOgo.png', 'rb')
        return HttpResponse(img.read(), content_type='image/bmp')

    @staticmethod
    @csrf_exempt
    def my_ava(request):
        if request.method == 'GET':
            username = request.user.username
            uid = models.UserInfo.objects.get(username=username).attachment_uuid
            if uid is None:
                img = open(settings.FILE_PATH + '9fb206a48683c9cc152534d3fe27bd95.jpeg', 'rb')
            else:
                attachment_name = models.Attachment.objects.get(attachment_uuid=uid).attachment_name
                img = open(settings.FILE_PATH + attachment_name, 'rb')
            return HttpResponse(img.read(), content_type='image/bmp')
        elif request.method == 'POST':
            pic = request.FILES.getlist('file')
            fileName = request.POST.get("fileName")
            username = request.user.username
            for item in pic:
                for i in item.chunks():
                    with open(settings.FILE_PATH + fileName, 'wb') as f:
                        f.write(i)
            uid = uuid.uuid4()
            models.Attachment.objects.create(attachment_name=fileName, attachment_uuid=uid)
            models.UserInfo.objects.filter(username=username).update(attachment_uuid=uid)
            return JsonResponse({'msg': 'success'}, safe=False)


class LoginOut:
    @staticmethod
    @verify_captcha
    def user_login(request):
        username = request.POST.get("username")
        userId = models.UserInfoView.objects.get(username=username).user_id
        password = request.POST.get('password')
        password = base64.b64decode(bytes(password, encoding='utf8'))
        with open('PestMessage/ssl.pem') as f:
            p = f.read()
            privateKey = rsa.PrivateKey.load_pkcs1(p)
        password = rsa.decrypt(password, privateKey).decode()[:-6]
        conn = get_redis_connection()
        if models.UserInfoView.objects.filter(user_id=userId).count():
            try:
                conn.hget('Info:' + str(userId), 'isFreeze').decode('utf-8')
            except:
                conn.hset('Info:' + str(userId), 'isFreeze', 0)
            if int(conn.hget('Info:' + str(userId), 'isFreeze').decode('utf-8')):
                return JsonResponse({'msg': '您的账号已经被冻结,请联系管理员解封'}, safe=False)
            else:
                username = models.UserInfoView.objects.get(user_id=userId).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    thisUser = {
                        'userId': userId,
                        'username': username,
                    }
                    token = Token.generate_token(thisUser)
                    return JsonResponse(
                        {'token': token, 'msg': '登录成功', 'username': username, 'csrf_token': csrf.get_token(request)},
                        safe=False)
                else:
                    conn.hincrby('Info:' + str(userId), 'loginCount')
                    if int(conn.hget('Info:' + str(userId), 'loginCount').decode('utf-8')) + 1 > 5:
                        conn.hset('Info:' + str(userId), 'isFreeze', 1)
                    return JsonResponse({'msg': '密码错误'}, safe=False)
        else:
            return JsonResponse({'msg': '没有你的账户'}, safe=False)

    @staticmethod
    @csrf_exempt
    def user_register(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            if models.UserInfoView.objects.filter(username=username).count():
                return JsonResponse({'msg': '你已经有账号啦'}, safe=False)
            else:
                if models.UserInfoView.objects.filter(username=username).count():
                    return JsonResponse({'msg': '名字已经被用过了'}, safe=False)
                else:
                    signature = '这个人很懒,什么都没有留下'
                    models.UserInfo.objects.create_user(username=username, password=password, signature=signature)
                    return JsonResponse({'msg': '注册成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def logout_view(request):
        logout(request)
        return JsonResponse({'msg': '退出成功'}, safe=False)

    @staticmethod
    @csrf_exempt
    def salt(request):
        salt = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        for i in range(6):
            salt += random.choice(chars)
        csrf_token = csrf.get_token(request)
        return JsonResponse({'salt': salt, 'csrf_token': csrf_token}, safe=False)


class UserInfo:

    @staticmethod
    @check_token
    @login_required
    def revise(request):
        if request.method == 'POST':
            oldPwd = request.POST.get('oldPwd')
            newPwd = request.POST.get('newPwd')
            if request.user.check_password(oldPwd):
                user = models.UserInfo.objects.get(username=request.user.username)
                user.password = hashers.make_password(newPwd)
                user.save()
                return JsonResponse({'msg': '修改成功'}, safe=False)
            else:
                return JsonResponse({'msg': '密码错误'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def my_info(request):
        conn = get_redis_connection()
        userId = request.user.id
        # userId = models.UserInfoView.objects.get(phoneNumber=phoneNumber).user_id
        response = UserInfo.ret_people_info(userId)
        try:
            newReplyNum = int(conn.hget('Info:' + str(userId), 'NRep').decode('utf-8'))
        except:
            newReplyNum = 0
        try:
            newLikeNum = int(conn.hget('Info:' + str(userId), 'NLike').decode('utf-8'))
        except:
            newLikeNum = 0
        try:
            newDisLikeNum = int(conn.hget('Info:' + str(userId), 'NDLike').decode('utf-8'))
        except:
            newDisLikeNum = 0
        response['data']['newReplyNum'] = newReplyNum
        response['data']['newLikeNum'] = newLikeNum
        response['data']['newDisLikeNum'] = newDisLikeNum
        return JsonResponse(response, safe=False)

    @staticmethod
    @check_token
    @login_required
    def people_info(request, userId):
        username = request.user.username
        response = UserInfo.ret_people_info(userId)
        response['data']['myName'] = username
        return JsonResponse(response, safe=False)

    @staticmethod
    def ret_people_info(userId):
        conn = get_redis_connection()
        username = models.UserInfoView.objects.get(user_id=userId).username
        try:
            commentsNum = int(conn.hget('Info:' + str(userId), 'CNum').decode('utf-8'))
        except:
            commentsNum = 0
        try:
            likeNum = int(conn.hget('Info:' + str(userId), 'LNum').decode('utf-8'))
        except:
            likeNum = 0
        try:
            disLikeNum = int(conn.hget('Info:' + str(userId), 'DLNum').decode('utf-8'))
        except:
            disLikeNum = 0
        signature = models.UserInfoView.objects.get(user_id=userId).signature
        if models.Volunteer.objects.filter(user_id=userId).count():
            isVolunteer = '1'
        else:
            isVolunteer = '0'
        response = {
            'msg': '成功',
            'data': {
                'name': username,
                'commentsNum': commentsNum,
                'likeNum': likeNum,
                'disLikeNum': disLikeNum,
                'signature': signature,
                'isVolunteer': isVolunteer,
            }
        }
        return response

    @staticmethod
    @check_token
    @login_required
    def signature(request):
        userId = request.user.id
        signature = request.POST.get('value')
        models.UserInfo.objects.filter(id=userId).update(signature=signature)
        return JsonResponse({'msg': '成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def volunteer(request):
        username = request.user.username
        phone = request.POST.get('phone')
        try:
            userId = models.UserInfoView.objects.get(username=username).user_id
        except:
            return JsonResponse({'msg': '此用户不存在'})
        qq = request.POST.get('qq')
        date1 = request.POST.get('date1')[16:25]
        date2 = request.POST.get('date2')[16:25]
        isDoctor = request.POST.get('isDoctor')
        if isDoctor:
            isDoctor = 1
        else:
            isDoctor = 0
        advantage = request.POST.get('advantage')
        words = request.POST.get('words')
        if models.Volunteer.objects.filter(user_id=userId).count():
            return JsonResponse({'msg': '您已经是志愿者了,不需要重复注册'}, safe=False)
        else:
            models.Volunteer.objects.create(username=username, user_id=userId, qqnum=qq, date1=date1, date2=date2,
                                            isdoctor=isDoctor, advantage=advantage, words=words, phone=phone)
            return JsonResponse({'msg': '注册成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def donation(request):
        username = request.user.username
        phone = request.POST.get('phone')
        try:
            userId = models.UserInfoView.objects.get(username=username).user_id
        except:
            return JsonResponse({'msg': '此用户不存在'})
        maskNum = request.POST.get('maskNum')
        proSuitNum = request.POST.get('proSuitNum')
        alcoholNum = request.POST.get('alcoholNum')
        convenientNum = request.POST.get('instantNum')
        waterNum = request.POST.get('waterNum')
        models.Donation.objects.create(username=username, user_id=userId, mask=maskNum, suit=proSuitNum,
                                       alcohol=alcoholNum, convenient=convenientNum, water=waterNum, phone=phone)
        return JsonResponse({'msg': '记录成功'}, safe=False)


@accept_websocket
def push_msg(request, username):
    conn = get_redis_connection()
    userId = request.user.id
    if request.is_websocket():
        while 1:
            time.sleep(3)
            try:
                newReplyNum = int(conn.hget('Info:' + str(userId), 'NRep').decode('utf-8'))
            except:
                newReplyNum = 0
            try:
                newLikeNum = int(conn.hget('Info:' + str(userId), 'NLike').decode('utf-8'))
            except:
                newLikeNum = 0
            try:
                newDisLikeNum = int(conn.hget('Info:' + str(userId), 'NDLike').decode('utf-8'))
            except:
                newDisLikeNum = 0
            if newReplyNum != 0 or newDisLikeNum != 0 or newLikeNum != 0:
                dit = {
                    'newReplyNum': newReplyNum,
                    'newLikeNum': newLikeNum,
                    'newDisLikeNum': newDisLikeNum
                }
                request.websocket.send(json.dumps(dit))
            try:
                msg = request.websocket.wait()
                request.websocket.send(msg)
            except:
                pass
