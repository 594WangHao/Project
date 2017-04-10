from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^api/register/$', views.register, name = 'api_register'),
    url(r'^api/login/$', views.login, name = 'api_login'),
    url(r'^api/logout/$', views.logout, name = 'api_logout'),
    url(r'^api/equip_data/', views.equip_data, name = 'api_equip_data'),
    url(r'^api/equip_info/', views.equip_info, name = 'api_equip_info'),
]