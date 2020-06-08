from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
from collections import Iterable
# Create your views here.
def show_login(request):
    return render(request,'login.html')

def show_regist(request):
    return render(request,'regist.html')


@csrf_exempt
def login_user(request):
    account = request.POST.get('user')
    passwd = request.POST.get('passwd')
    results = User.objects.filter(username=account)
    print(results)
    print(isinstance(results,Iterable))
    obj = None
    for item in results:
        obj = item
    print(obj)
    if obj:
        if obj.password == passwd:
            msg = {'code': 200, 'infor': 'login success'}
        else:
            msg = {'code': 400, 'infor': 'password failed'}
    else:
        msg = {'code': 300, 'infor': '该账号不存在'}
    return HttpResponse(json.dumps(msg))

@csrf_exempt
def regist_user(request):
    user = request.POST.get('user')
    passwd = request.POST.get('passwd')

    if user is '' or passwd is '':
        msg = {'code':300,'infor':'请输入账号或密码'}
        return HttpResponse(json.dumps(msg))
    results = User.objects.filter(username=user)
    print(results)
    obj = None
    for result in results:
        print('this is a test')
        obj = result
    if obj is None:
        User.objects.create(username=user,password=passwd)
        msg = {'code':200,'infor':'账号注册成功'}
    else:
        # User.objects.all().first().delete()
        request.session['username'] = user
        # del request.session['username']
        print(request.session.get('username'))
        msg = {'code':400,'infor':'该账号已存在'}
    return HttpResponse(json.dumps(msg))