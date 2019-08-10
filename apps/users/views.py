from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout  # 自带的权限认证函数
from django.http import HttpResponseRedirect, JsonResponse    # url重定向
from django.urls import reverse

from apps.users.forms import LoginForm, DynamicLoginForm    # 登录验证from表单
from apps.utils.random_str import generate_random   # 生成验证码
from apps.utils.YunPian import send_single_sms  # 云片网发送验证码
from MxOnline.settings import yp_apikey  # 引入云片网配置

# 登录
class LoginView(View):
    def get(self, request, *args, **kwargs):
        # 判断用户是否登录
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))  # 跳转url地址
        # 返回图片验证码
        login_form = DynamicLoginForm()
        return render(request, 'login.html', {
            "login_form": login_form
        })

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


# 退出登录
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


# 验证码
class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data["mobile"]
            #随机生成数字验证码
            code = generate_random(4, 0)
            re_json = send_single_sms(yp_apikey, code, mobile=mobile)
            if re_json["code"] == 0:
                re_dict["status"] = "success"
                # r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
                # r.set(str(mobile), code)
                # r.expire(str(mobile), 60*5) #设置验证码五分钟过期
            else:
                re_dict["msg"] = re_json["msg"]
        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]

        return JsonResponse(re_dict)

