from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from perfil import views

urlpatterns = [
    re_path(r'^perfil/$', views.Profile.as_view() ),
    re_path(r'^perfil/(?P<id>\d+)$', views.Profile.as_view() ),
]