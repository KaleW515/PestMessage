import base64
import json
import random
import time

import itsdangerous
import requests
import rsa
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth import authenticate, hashers, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
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
            date = request.POST.get('date')
            keyWordsList = models.KeyWords.objects.all().values_list()
            for item in keyWordsList:
                if item[1] in content:
                    return JsonResponse({'msg': '含有屏蔽关键字'}, safe=False)
            try:
                phoneNumber = request.user.phoneNumber
                name = request.user.username
                models.Reply.objects.create(from_phonenumber=phoneNumber, to_commentsid=commentsId, from_name=name,
                                            date=date,
                                            content=content)
                response = {
                    'msg': '评论成功',
                    'name': name,
                }
                thePhoneNum = models.Comments.objects.get(id=commentsId).from_phonenumber
                conn.hincrby('Info:' + thePhoneNum, 'NRep')
                return JsonResponse(response, safe=False)
            except:
                return JsonResponse({'msg': '你还没登录啊'}, safe=False)

        elif request.method == 'GET':
            commentsId = int(request.GET.get('commentsId'))
            ls = []
            try:
                result = models.Reply.objects.filter(to_commentsid=commentsId).values()
                for item in result:
                    item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + item['from_name']
                    ls.append(item)
                p = Paginator(ls, len(ls))
                pageNow = p.page(1).object_list
                return JsonResponse(pageNow, safe=False)
            except:
                return JsonResponse({'msg': '没有回复'}, safe=False)

        elif request.method == 'DELETE':
            replyId = int(request.GET.get('id'))
            models.Reply.objects.filter(id=replyId).delete()
            return JsonResponse({'msg': '成功'}, safe=False)


class LikeAndDisLike:

    @staticmethod
    @check_token
    @login_required
    def inc_like_num(request):
        commentsId = int(request.POST.get('commentsId'))
        phoneNumber = request.user.phoneNumber
        conn = get_redis_connection()
        if bytes(phoneNumber, encoding='utf-8') in conn.smembers('like:' + str(commentsId)):
            return JsonResponse({'msg': '你已经点过赞啦'}, safe=False)
        else:
            conn.sadd('like:' + str(commentsId), phoneNumber)
            likeNum = models.Comments.objects.get(id=commentsId).likenum + 1
            models.Comments.objects.filter(id=commentsId).update(likenum=likeNum)
            thePhoneNum = models.Comments.objects.get(id=commentsId).from_phonenumber
            conn.hincrby('Info:' + thePhoneNum, 'LNum')
            conn.hincrby('Info:' + thePhoneNum, 'NLike')
            return JsonResponse({'msg': '点赞成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def inc_dislike_num(request):
        commentsId = int(request.POST.get('commentsId'))
        phoneNumber = request.user.phoneNumber
        conn = get_redis_connection()
        if bytes(phoneNumber, encoding='utf-8') in conn.smembers('DLike:' + str(commentsId)):
            return JsonResponse({'msg': '你已经点过踩啦'}, safe=False)
        else:
            conn.sadd('DLike:' + str(commentsId), phoneNumber)
            disLikeNum = models.Comments.objects.get(id=commentsId).dislikenum + 1
            models.Comments.objects.filter(id=commentsId).update(dislikenum=disLikeNum)
            thePhoneNum = models.Comments.objects.get(id=commentsId).from_phonenumber
            conn.hincrby('Info:' + thePhoneNum, 'DLNum')
            conn.hincrby('Info:' + thePhoneNum, 'NDLike')
            return JsonResponse({'msg': '点踩成功'}, safe=False)


class Comments:

    @staticmethod
    @check_token
    @login_required
    def personal_comments(request):
        if request.method == 'POST':
            conn = get_redis_connection()
            if request.POST.get('phoneNumber') is not None:
                phoneNumber = request.POST.get('phoneNumber')
            else:
                phoneNumber = request.user.phoneNumber
            ls = []
            result = models.Comments.objects.filter(from_phonenumber=phoneNumber).values()
            for item in result:
                item['reply'] = []
                item['inputIsShow'] = False
                item['replyIsShow'] = False
                item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + item['name']
                ls.append(item)
            p = Paginator(ls, 5)
            conn.hset('Info:' + phoneNumber, 'NRep', 0)
            conn.hset('Info:' + phoneNumber, 'NLike', 0)
            conn.hset('Info:' + phoneNumber, 'NDLike', 0)
            currentPage = request.POST.get('currentPage')
            if int(currentPage) > p.num_pages:
                return JsonResponse({'msg': '已经没有啦', 'pageCount': str(p.num_pages)}, safe=False)
            else:
                pageNow = p.page(int(currentPage)).object_list
                return JsonResponse({'msg': '成功', 'pageCount': str(p.num_pages), 'pageNow': pageNow}, safe=False)

        elif request.method == 'DELETE':
            commentId = request.GET.get('commentId')
            try:
                models.Comments.objects.filter(id=commentId).delete()
                models.Reply.objects.filter(to_commentsid=commentId).delete()
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
                    if field in item['content']:
                        item['reply'] = []
                        item['inputIsShow'] = False
                        item['replyIsShow'] = False
                        item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + item['name']
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
                    item['reply'] = []
                    item['inputIsShow'] = False
                    item['replyIsShow'] = False
                    item['avaUrl'] = settings.BASE_IMG_URL + 'people_ava/' + item['name']
                    ls.append(item)
                if value == 'true':
                    ls = sorted(ls, key=lambda ls: ls["likenum"], reverse=True)
                else:
                    ls.reverse()
                p = Paginator(ls, 10)
                if int(currentPage) > p.num_pages:
                    return JsonResponse({'msg': '已经没有啦', 'pageCount': str(p.num_pages)}, safe=False)
                else:
                    pageNow = p.page(int(currentPage)).object_list
                    return JsonResponse(
                        {'msg': '成功', 'pageCount': str(p.num_pages), 'pageNow': pageNow,
                         'username': request.user.username},
                        safe=False)

    @staticmethod
    @check_token
    @login_required
    def writer_message(request):
        conn = get_redis_connection()
        myComments = request.POST.get('myComments')
        date = request.POST.get('date')
        username = request.user.username
        keyWordsList = models.KeyWords.objects.all().values_list()
        for item in keyWordsList:
            if item[1] in myComments:
                return JsonResponse({'msg': '含有屏蔽关键字'}, safe=False)
        try:
            phoneNumber = request.user.phoneNumber
            models.Comments.objects.create(from_phonenumber=phoneNumber, likenum=0, dislikenum=0, content=myComments,
                                           date=date, name=username)
            conn.hincrby('Info:' + phoneNumber, 'CNum')
            return JsonResponse({'msg': '发表成功'}, safe=False)
        except:
            return JsonResponse({'msg': '你还没登录啊'}, safe=False)


class Avatar:

    @staticmethod
    @login_required
    def people_ava(request, username):
        if request.method == 'GET':
            try:
                img = open('templates/Files/images/' + username + '.jpeg', 'rb')
            except:
                img = open('templates/Files/images/9fb206a48683c9cc152534d3fe27bd95.jpeg', 'rb')
            return HttpResponse(img.read(), content_type='image/bmp')

    @staticmethod
    @login_required
    def vol_logo(request):
        img = open('templates/Files/images/vounteerLOgo.png', 'rb')
        return HttpResponse(img.read(), content_type='image/bmp')

    @staticmethod
    def my_ava(request):
        if request.method == 'GET':
            username = request.user.username
            try:
                img = open('templates/Files/images/' + username + '.jpeg', 'rb')
            except:
                img = open('templates/Files/images/9fb206a48683c9cc152534d3fe27bd95.jpeg', 'rb')
            return HttpResponse(img.read(), content_type='image/bmp')
        elif request.method == 'POST':
            pic = request.FILES.getlist('file')
            username = request.user.username
            for item in pic:
                for i in item.chunks():
                    fileName = username + '.jpeg'
                    with open('templates/Files/images/' + fileName, 'wb') as f:
                        f.write(i)
            return JsonResponse({'msg': 'success'}, safe=False)


class LoginOut:
    @staticmethod
    @verify_captcha
    def user_login(request):
        phoneNumber = request.POST.get('phoneNumber')
        password = request.POST.get('password')
        password = base64.b64decode(bytes(password, encoding='utf8'))
        with open('PestMessage/ssl.pem') as f:
            p = f.read()
            privateKey = rsa.PrivateKey.load_pkcs1(p)
        password = rsa.decrypt(password, privateKey).decode()[:-6]
        conn = get_redis_connection()
        if models.UserInfoView.objects.filter(phoneNumber=phoneNumber).count():
            try:
                conn.hget('Info:' + phoneNumber, 'isFreeze').decode('utf-8')
            except:
                conn.hset('Info:' + phoneNumber, 'isFreeze', 0)
            if int(conn.hget('Info:' + phoneNumber, 'isFreeze').decode('utf-8')):
                return JsonResponse({'msg': '您的账号已经被冻结,请联系管理员解封'}, safe=False)
            else:
                username = models.UserInfoView.objects.get(phoneNumber=phoneNumber).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    thisUser = {
                        'phoneNumber': phoneNumber,
                        'name': password,
                        'username': username,
                    }
                    token = Token.generate_token(thisUser)
                    return JsonResponse({'token': token, 'msg': '登录成功', 'username': username}, safe=False)
                else:
                    conn.hincrby('Info:' + phoneNumber, 'loginCount')
                    if int(conn.hget('Info:' + phoneNumber, 'loginCount').decode('utf-8')) + 1 > 5:
                        conn.hset('Info:' + phoneNumber, 'isFreeze', 1)
                    return JsonResponse({'msg': '密码错误'}, safe=False)
        else:
            return JsonResponse({'msg': '没有你的账户'}, safe=False)

    @staticmethod
    def user_register(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            phoneNumber = request.POST.get('phoneNumber')
            password = request.POST.get('pass')
            if models.UserInfoView.objects.filter(phoneNumber=phoneNumber).count():
                return JsonResponse({'msg': '你已经有账号啦'}, safe=False)
            else:
                if models.UserInfoView.objects.filter(username=username).count():
                    return JsonResponse({'msg': '名字已经被用过了'}, safe=False)
                else:
                    signature = '这个人很懒,什么都没有留下'
                    models.UserInfo.objects.create_user(username=username, password=password,
                                                        phoneNumber=phoneNumber, signature=signature)
                    return JsonResponse({'msg': '注册成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def logout_view(request):
        logout(request)
        return JsonResponse({'msg': '退出成功'}, safe=False)

    @staticmethod
    def salt(request):
        salt = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        for i in range(6):
            salt += random.choice(chars)
        return JsonResponse({'salt': salt}, safe=False)


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
        phoneNumber = request.user.phoneNumber
        response = UserInfo.ret_people_info(phoneNumber)
        try:
            newReplyNum = int(conn.hget('Info:' + phoneNumber, 'NRep').decode('utf-8'))
        except:
            newReplyNum = 0
        try:
            newLikeNum = int(conn.hget('Info:' + phoneNumber, 'NLike').decode('utf-8'))
        except:
            newLikeNum = 0
        try:
            newDisLikeNum = int(conn.hget('Info:' + phoneNumber, 'NDLike').decode('utf-8'))
        except:
            newDisLikeNum = 0
        response['data']['newReplyNum'] = newReplyNum
        response['data']['newLikeNum'] = newLikeNum
        response['data']['newDisLikeNum'] = newDisLikeNum
        return JsonResponse(response, safe=False)

    @staticmethod
    @check_token
    @login_required
    def people_info(request, phoneNumber):
        username = request.user.username
        response = UserInfo.ret_people_info(phoneNumber)
        response['data']['myName'] = username
        return JsonResponse(response, safe=False)

    @staticmethod
    def ret_people_info(phoneNumber):
        conn = get_redis_connection()
        username = models.UserInfoView.objects.get(phoneNumber=phoneNumber).username
        try:
            commentsNum = int(conn.hget('Info:' + phoneNumber, 'CNum').decode('utf-8'))
        except:
            commentsNum = 0
        try:
            likeNum = int(conn.hget('Info:' + phoneNumber, 'LNum').decode('utf-8'))
        except:
            likeNum = 0
        try:
            disLikeNum = int(conn.hget('Info:' + phoneNumber, 'DLNum').decode('utf-8'))
        except:
            disLikeNum = 0
        signature = models.UserInfoView.objects.get(phoneNumber=phoneNumber).signature
        if models.Volunteer.objects.filter(phonenumber=phoneNumber).count():
            isVolunteer = '1'
        else:
            isVolunteer = '0'
        response = {
            'msg': '成功',
            'data': {
                'name': username,
                'phoneNumber': phoneNumber,
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
        phoneNumber = request.user.phoneNumber
        signature = request.POST.get('value')
        models.UserInfo.objects.filter(phoneNumber=phoneNumber).update(signature=signature)
        return JsonResponse({'msg': '成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def volunteer(request):
        username = request.POST.get('name')
        phoneNumber = request.POST.get('phoneNumber')
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
        if models.Volunteer.objects.filter(phonenumber=phoneNumber).count():
            return JsonResponse({'msg': '您已经是志愿者了,不需要重复注册'}, safe=False)
        else:
            models.Volunteer.objects.create(name=username, phonenumber=phoneNumber, qqnum=qq, date1=date1, date2=date2,
                                            isdoctor=isDoctor, advantage=advantage, words=words)
            return JsonResponse({'msg': '注册成功'}, safe=False)

    @staticmethod
    @check_token
    @login_required
    def donation(request):
        username = request.POST.get('name')
        phoneNumber = request.POST.get('phoneNumber')
        maskNum = request.POST.get('maskNum')
        proSuitNum = request.POST.get('proSuitNum')
        alcoholNum = request.POST.get('alcoholNum')
        instantNum = request.POST.get('instantNum')
        waterNum = request.POST.get('waterNum')
        models.Donation.objects.create(name=username, phonenumber=phoneNumber, mask=maskNum, suit=proSuitNum,
                                       alcohol=alcoholNum, instant=instantNum, water=waterNum)
        return JsonResponse({'msg': '记录成功'}, safe=False)


@accept_websocket
def push_msg(request, username):
    conn = get_redis_connection()
    phoneNumber = request.user.phoneNumber
    if request.is_websocket():
        while 1:
            time.sleep(3)
            try:
                newReplyNum = int(conn.hget('Info:' + phoneNumber, 'NRep').decode('utf-8'))
            except:
                newReplyNum = 0
            try:
                newLikeNum = int(conn.hget('Info:' + phoneNumber, 'NLike').decode('utf-8'))
            except:
                newLikeNum = 0
            try:
                newDisLikeNum = int(conn.hget('Info:' + phoneNumber, 'NDLike').decode('utf-8'))
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
