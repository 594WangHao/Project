from django.contrib import admin
from .models import Data, Equipment

# Register your models here.
admin.AdminSite.site_header = '用户/设备管理系统'

admin.site.register(Equipment)
# admin.site.register(Data)