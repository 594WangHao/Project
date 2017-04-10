from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.serializers.json import DjangoJSONEncoder

from .models import Data, Equipment
from .utils import REST_response

import numpy as np


# 首页
def index(request):
    return render(request, 'index.html', {'is_authenticated': True})


# 登录接口 POST
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return REST_response()
        else:
            # Return a 'disabled account' error message
            return REST_response(101, '没有访问权限')
    else:
        # Return an 'invalid login' error message.
        return REST_response(102, '用户名或密码错误')


# 登出接口 GET
def logout(request):
    auth_logout(request)
    return REST_response()

# 注册接口 POST
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    email = request.POST['email']
    if password != password2:
        return REST_response(103, '密码不一致')
    try:
        user = User.objects.get(username = username)
    except (KeyError,User.DoesNotExist):
        user = User.objects.create_user(username, email, password)
        user.save()
        auth_login(request, user)
        return REST_response()
    else:
        return REST_response(104, '用户名重复')


# 设备信息 GET
def equip_info(request):
    equip_id = request.GET['equip']

    try:
        equip = Equipment.objects.get(id = equip_id)
    except (KeyError, Equipment.DoesNotExist):
        return REST_response(201, '未找到相关设备')
    else:
        data = {
            'name': equip.name,
            'point_number': equip.point_number,
            'seat': equip.seat,
            'device': equip.device,
            'add_time': str(equip.add_time),
            'remarks': equip.remarks,
        }

        # response = simplejson.dumps(response_obj)
        return REST_response(data = data)

# 数据接口 GET 5s轮询
def equip_data(request):
    equip = request.GET['equip']
    point = request.GET['point']
    start = int(request.GET['start'])
    end = int(request.GET['end'])

    data_list = Data.objects.filter(equipment = equip, point = point, id__range = (start, end))
    if (len(data_list) <= 0):
        return REST_response(202, '未找到相关数据')
    else:
        sinx = []
        for obj in data_list:
            sinx.append(obj.y)

        # 傅里叶变换
        nSampleNum = 5120
        ncount = 1024
        df = nSampleNum / ncount

        fft = np.fft.fft(sinx)
        fftx = np.linspace(start, df * (end - start + 1 ), (end - start + 1))

        response_obj = {
            'original_data':[],
            'fft_data': [],
        }
        for original in data_list:
            response_obj['original_data'].append({
                'x': original.x,
                'y': original.y
            })

        for i in range(len(fft)):
            response_obj['fft_data'].append({
                'x': fftx[i],
                'y': abs(fft[i])
            })
        # response = simplejson.dumps(response_obj)

        return REST_response(data = response_obj)


# def create_data():
#     print('开始生成数据')
#     import numpy as np
#     from matplotlib import pyplot as plt

#     nSampleNum = 5120
#     ncount = 1024.0
#     df = nSampleNum / ncount
#     sampleTime = ncount / nSampleNum
#     freqLine = 800

#     x = np.linspace(0, sampleTime, ncount)

#     # 三个标准正弦波形
#     sinx = np.sin(2 * np.pi * 250 * x)
#     sinx2 = 0.5 * np.sin(2 * np.pi * 500 * x)
#     sinx3 = 0.3 * np.sin(2 * np.pi * 1000 * x)

#     # 叠加时域
#     sinx += sinx2
#     sinx += sinx3

#     i = 0
#     e = Equipment.objects.get(pk = 1)
#     while i  < len(x):
#         if i % 100 == 0:
#             print(i)
#         data = Data(equipment = e, x = x[i], y = sinx[i])
#         data.save()
#         i+= 1

#     print('生成数据完成')


# def delete_data():
#     Data.objects.all().delete()
#     print('清空数据')

