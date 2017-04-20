from django.http import HttpResponse
from django.shortcuts import render

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class UserCheck(MiddlewareMixin):
    """
    用户登录检查中间件
    """
    def process_request(self, request):
        path = request.path
        if (path == '/') or (path == '/api/equip_data/') or (path == '/api/equip_info') or (path == '/api/equip_list/') :
             if not request.user.is_authenticated():
                return render(request, 'index.html', {'is_authenticated': False})


