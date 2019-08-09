# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/8/9  18:44'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, required=True)
    password = forms.CharField(min_length=2, required=True)
