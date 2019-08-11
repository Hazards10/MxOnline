"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt    # 去除单个views函数的csrf验证
from django.views.static import serve  # 为目录中的静态文件提供服务

import xadmin

from apps.users.views import LoginView, LogoutView, SendSmsView, DynamicLoginView, RegisterView
from apps.organizations.views import OrgView
from MxOnline.settings import MEDIA_ROOT  # 引入media上传路径

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('ueditor/', include('DjangoUeditor.urls')),
    path('xadmin/', xadmin.site.urls),  # xadmin
    path('', TemplateView.as_view(template_name="index.html"), name="index"),  # 首页
    path('login/', LoginView.as_view(), name="login"),  # 登录
    path('register/', RegisterView.as_view(), name="register"),  # 注册
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),  # 动态验证码登录
    path('logout/', LogoutView.as_view(), name="logout"),   # 退出登录
    url(r'^captcha/', include('captcha.urls')),     # 图片验证码
    url(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),  # 发送图片验证码
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 配置上传文件的访问url
    path('org_list/', OrgView.as_view(), name="org_list"),  # 机构列表页

]
