from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from empleado import views

urlpatterns = [
    re_path(r'^negocios/$', views.NegociosList.as_view() ),
    #re_path(r'^sucursal/(?P<id>\d+)$', views.SucursalDetail.as_view() ),
]