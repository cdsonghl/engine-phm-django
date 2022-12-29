from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
# Create your views here.

def login(request):
    # 登录界面
    if request.method == 'GET':
        return render(request, '../templates/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('用户名或密码错误')
        if password != user.password:
            return HttpResponse('用户名或密码错误')

        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        # 判断用户是否选择了记住用户名，选了的话cookies存储3天
        return HttpResponseRedirect('/phmsite')

def register(request):
    # 注册
    # get 返回页面
    # post 处理提交数据 1.两个密码保持一致 2. 当前用户名是否可用
    if request.method == 'GET':
        return render(request, '../templates/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username is None:
            return  HttpResponse('用户名不能为空')
        if password1 != password2:
            return HttpResponse('两次密码输入不一致')
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已注册')

        try:
            User.objects.create(username=username, password=password1)
        except Exception as e:
            print('--create user error %s'%(e))
            return HttpResponse('用户名已注册')

        return HttpResponse('注册成功')


def logout(request):
    # 注销登录
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    # 删除cookies
    resp = HttpResponseRedirect('/phmsite')
    if 'username' in request.COOKIES:
        resp.delete_cookie('usename')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp

