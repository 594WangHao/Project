import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")
django.setup()

from app.models import Data, Equipment, Point
from django.utils import timezone

import datetime

import numpy as np


def create_data():
    print('开始生成数据')
    import numpy as np

    nSampleNum = 5120 / 2
    ncount = 1024.0
    df = nSampleNum / ncount
    sampleTime = ncount / nSampleNum


    x = np.linspace(0, sampleTime, ncount)

    # 三个标准正弦波形
    sinx = np.sin(2 * np.pi * 250 * x)
    sinx2 = 0.5 * np.sin(2 * np.pi * 500 * x)
    sinx3 = 0.3 * np.sin(2 * np.pi * 1000 * x)

    # 叠加时域
    sinx += sinx2
    sinx += sinx3

    i = 0
    equipments = Equipment.objects.all()
    time = timezone.now()

    while i < len(equipments):
        equipment = equipments[i]
        points = Point.objects.filter(equipment = equipment)
        j = 0
        while j < len(points):
            point = points[j]
            k = 0
            data_list = []
            while k < len(x) * (60 * 60 * 8) :
                time += datetime.timedelta(microseconds = 976.5625)

                data = Data(equipment = equipment, point = point, amplitude = sinx[k % len(x)], add_time = time)

                data_list.append(data)

                if k % (1024 * 60 * 15) == 0:
                    print('设备: %s, 测点: %s, 已生成: %d ' % (equipment.name, point.number, k))
                    Data.objects.bulk_create(data_list)
                    data_list = []
                    print('设备: %s, 测点: %s , %d 小时数据已存储' % (equipment.name, point.number, k / (1024 * 60 * 60)))
                k += 1

            j += 1
        i += 1

    print('生成数据完成')


def delete_data():
    Data.objects.all().delete()
    print('清空数据')

create_data()
# delete_data()