from django.contrib import admin
from .models import Equipment, Point, Data

# Register your models here.
admin.AdminSite.site_header = '用户&设备管理系统'

class PointInline(admin.TabularInline):
    model = Point
    extra = 1

class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['add_time']
    inlines = [PointInline]


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Data)

