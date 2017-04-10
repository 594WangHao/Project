from django.http import HttpResponse

import simplejson

# 错误号, 错误信息

# 用户部分
# 101,    没有访问权限
# 102,    用户名或密码错误
# 103,    密码不一致
# 104,    用户名重复

# 设备部分
# 201,    未找到相关设备
# 202,    未找到相关数据


def REST_response(code = 100, message = 'success', data = {}):
    response_obj = {
        'code': code,
        'message': message,
        'data': data
    }
    response = simplejson.dumps(response_obj)

    return HttpResponse(response, content_type = 'application/json')