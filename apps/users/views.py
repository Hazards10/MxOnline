from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login  # 自带的权限认证函数
from django.http import HttpResponseRedirect    # url重定向
from django.urls import reverse


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))  # 跳转url地址
        else:
            return render(request, 'login.html', {
                'msg': "用户名或密码错误"
            })


