from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from alumno import views

urlpatterns = [
    re_path(r'^alumnos/$', views.AlumnosList.as_view() ),
    re_path(r'^profesores/$', views.ProfesorList.as_view() ),
]