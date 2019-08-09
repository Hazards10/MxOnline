from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout  # 自带的权限认证函数
from django.http import HttpResponseRedirect    # url重定向
from django.urls import reverse

from apps.users.forms import LoginForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        # 判断用户是否登录
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))  # 跳转url地址
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # django表单验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))  # 跳转url地址
            else:
                return render(request, 'login.html', {
                    'msg': "用户名或密码错误",
                    'login_form': login_form
                })
        else:
            return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))



