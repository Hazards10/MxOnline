# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/8/9  18:44'

from django import forms
from captcha.fields import CaptchaField    # django-captcha-simple 图片验证码
import redis  # 引入redis数据库
from MxOnline.settings import REDIS_HOST, REDIS_PORT  # 引入redis配置

from apps.users.models import UserProfile


# 登录验证form
class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, required=True)
    password = forms.CharField(min_length=2, required=True)


# 动态登录验证form(图片验证码)
class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


# 动态登录验证form(数字验证码)
class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    # 这个方法先与clean（self）执行
    def clean_code(self):
        mobile = self.data.get("mobile")
        code = self.data.get("code")
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError("验证码不正确")
        return self.cleaned_data

    # 不能验证是哪个字段的错误
    # def clean(self):
    #     mobile = self.cleaned_data["mobile"]
    #     code = self.cleaned_data["code"]
    #     r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
    #     redis_code = r.get(str(mobile))
    #     if code != redis_code:
    #         raise forms.ValidationError("验证码不正确")
    #     return self.cleaned_data


# 注册验证图片验证码form
class RegisterGetForm(forms.Form):
    captcha = CaptchaField()


# 注册手机验证验证
class RegisterPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)
    password = forms.CharField(required=True)

    def clean_mobile(self):
        mobile = self.data.get("mobile")
        # 验证手机号码是否已经注册
        users = UserProfile.objects.filter(mobile=mobile)
        if users:
            raise forms.ValidationError("该手机号码已注册")
        return mobile

    def clean_code(self):
        mobile = self.data.get("mobile")
        code = self.data.get("code")
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError("验证码不正确")
        return code
