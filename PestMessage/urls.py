"""PestMessage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from PestApp import views
from rest_framework.routers import DefaultRouter


urlpatterns = (
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    url(r'^captcha/', include('captcha.urls')),
    url('refreshCaptcha', views.Captcha.refreshCaptcha),
    url('getNewMsg', views.getNewMsg),
    url('img', views.RetImg.retImg),
    url('getDonation', views.UserInfo.getDonation),
    url('toBeVolunteer', views.UserInfo.toBeVolunteer),
    url('writeMessage', views.Comments.writerMessage),
    url('writeReply', views.ReplyRelation.writerReply),
    url('incLikeNum', views.LikeAndDisLike.incLikeNum),
    url('incDisLikeNum', views.LikeAndDisLike.incDisLikeNum),
    url('watchReply', views.ReplyRelation.watchReply),
    url('watchComments', views.Comments.watchComments),
    url('watchMoreComments', views.Comments.watchMoreComments),
    url('login', views.LoginOut.userLogin),
    url('salt', views.LoginOut.createSalt),
    url('register', views.LoginOut.userRegister),
    url('logout', views.LoginOut.logoutView),
    url('getMyInfo', views.UserInfo.getMyInfo),
    url('watchMyReply', views.ReplyRelation.watchMyReply),
    url('deleteMyComments', views.Comments.deleteMyComments),
    url('delMyReply', views.ReplyRelation.delMyReply),
    url('VolLogo', views.Avatar.getVolLogo),
    url('revise', views.UserInfo.revise),
    url('searchComments', views.Comments.searchComments),
    url('myPic', views.Avatar.saveMyAva),
    url('getMyAva', views.Avatar.getMyAva),
    url('getCommentsAva', views.Avatar.getCommentsAva),
    url('mySignatureRevise', views.UserInfo.mySignatureRevise),
    url('getOtherInfo', views.UserInfo.getOtherInfo),
    url('getOtherAva', views.Avatar.getOtherAva),
    url('pushMsg', views.pushMsg),
)
