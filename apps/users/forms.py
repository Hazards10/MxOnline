# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/8/9  18:44'

from django import forms
from captcha.fields import CaptchaField    # django-captcha-simple 图片验证码


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, required=True)
    password = forms.CharField(min_length=2, required=True)


class DynamicLoginForm(forms.Form):
    captcha = CaptchaField()