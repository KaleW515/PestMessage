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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^refresh_captcha', views.Captcha.refresh_captcha),
    url(r'^new_msg', views.new_msg),
    url(r'^img', views.RetImg.ret_img),
    url(r'^donation', views.UserInfo.donation),
    url(r'^volunteer', views.UserInfo.volunteer),
    url(r'^write_message', views.Comments.writer_message),
    url(r'^inc_like_num', views.LikeAndDisLike.inc_like_num),
    url(r'^inc_dislike_num', views.LikeAndDisLike.inc_dislike_num),
    url(r'^reply', views.Reply.reply),
    url(r'^comments', views.Comments.comments),
    url(r'^login', views.LoginOut.user_login),
    url(r'^salt', views.LoginOut.salt),
    url(r'^register', views.LoginOut.user_register),
    url(r'^logout', views.LoginOut.logout_view),
    url(r'^my_info', views.UserInfo.my_info),
    url(r'^personal_comments', views.Comments.personal_comments),
    url(r'^vol_logo', views.Avatar.vol_logo),
    url(r'^revise', views.UserInfo.revise),
    url(r'^my_ava', views.Avatar.my_ava),
    url(r'^people_ava/(?P<username>\w+)', views.Avatar.people_ava),
    url(r'^signature', views.UserInfo.signature),
    url(r'^people_info/(?P<phoneNumber>\w+)', views.UserInfo.people_info),
    url(r'^push_msg/(?P<username>\w+)', views.push_msg),
]
