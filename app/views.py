from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

from .models import Data, Equipment, Point
from .utils import REST_response

import datetime

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
            'name':equip.name ,
            'workshop':equip.workshop ,
            'seat':equip.seat ,
            'abline':equip.abline ,
            'add_time':str(equip.add_time) ,
            'remarks':equip.remarks ,
        }

        # response = simplejson.dumps(response_obj)
        return REST_response(data = data)

# 数据接口 GET
def equip_data(request):
    equip = request.GET['equip']
    point = request.GET['point']
    start = request.GET['start']
    end = request.GET['end']

    data_list = Data.objects.filter(equipment = equip, point = point, add_time__range = [datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S'), datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')])
    if (len(data_list) <= 0):
        return REST_response(202, '未找到相关数据')
    else:
        sinx = []
        for obj in data_list:
            sinx.append(obj.amplitude)

        # 傅里叶变换
        nSampleNum = 5120 / 2
        ncount = 1024
        df = nSampleNum / ncount
        sampleTime = ncount / nSampleNum
        freqLine = len(data_list) // 2

        fft = np.fft.fft(sinx)[0:freqLine]
        fftx = np.linspace(0, df * len(data_list), len(data_list))

        response_obj = {
            'original_data':[],
            'fft_data': [],
        }
        for original in data_list:
            response_obj['original_data'].append({
                'add_time': str(original.add_time),
                'amplitude': original.amplitude
            })

        for i in range(len(fft)):
            response_obj['fft_data'].append({
                'x': fftx[i],
                'y': abs(fft[i])
            })
        # response = simplejson.dumps(response_obj)

        return REST_response(data = response_obj)

# 设备列表
def equip_list(request):
    try:
        equips = Equipment.objects.all()
    except (KeyError, Equipment.DoesNotExist):
        return REST_response(203, '设备列表为空')
    else:
        i = 0
        data = []

        while i < len(equips):

            points = Point.objects.filter(equipment = equips[i])
            points_data = []
            j = 0
            while j < len(points):
                points_data.append({
                    "id": points[j].id,
                    "number": points[j].number,
                    "level": points[j].level,
                    "direction": points[j].direction,
                    "warning_line": points[j].warning_line,
                    "danger_line": points[j].danger_line,
                    "add_time": str(points[j].add_time),
                })
                j += 1

            data.append({
                'id': equips[i].id,
                'name':equips[i].name,
                'workshop':equips[i].workshop ,
                'seat':equips[i].seat ,
                'abline':equips[i].abline ,
                'add_time':str(equips[i].add_time) ,
                'remarks':equips[i].remarks ,
                'points': points_data
            })
            i += 1

        return REST_response(data = data)

# 为适应 vue-charts 单独做一个接口
def equip_data_vue_charts(request):
    equip = request.GET['equip']
    point = request.GET['point']
    start = request.GET['start']
    end = request.GET['end']
    print(datetime.strptime(start,'%Y-%m-%d %H:%M:%S'), datetime.strptime(end,'%Y-%m-%d %H:%M:%S'))
    data_list = Data.objects.filter(equipment = equip, point = point, add_time__range = [datetime.strptime(start,'%Y-%m-%d %H:%M:%S'), datetime.strptime(end,'%Y-%m-%d %H:%M:%S')])
    if (len(data_list) <= 0):
        return REST_response(202, '未找到相关数据')
    else:
        sinx = []
        for obj in data_list:
            sinx.append(obj.amplitude)

        # 傅里叶变换
        nSampleNum = 5120 / 2
        ncount = 1024
        df = nSampleNum / ncount
        sampleTime = ncount / nSampleNum
        freqLine = len(data_list) // 2

        fft = np.fft.fft(sinx)[0:freqLine]
        fftx = np.linspace(0, df * len(data_list), len(data_list))

        response_obj = {
            'original_data':[],
            'fft_data': [],
        }
        for original in data_list:
            response_obj['original_data'].append([
                str(original.add_time),
                original.amplitude
            ])

        for i in range(len(fft)):
            response_obj['fft_data'].append([
                fftx[i],
                abs(fft[i])
            ])


        return REST_response(data = response_obj)
