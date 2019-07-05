

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404


from empleado.models import Empleado
from empleado.serializers import EmpleadoSerializer

from alumno.models import Alumno
from alumno.serializers import AlumnoSerializer

from alumno.models import Profesor
from alumno.serializers import ProfesorSerializer
class AlumnosList(APIView):
    
    def post(self, request, format=None):
        serializer = AlumnoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        queryset =  Alumno.objects.filter(status=0)
        serializer = AlumnoSerializer(queryset, many=True)
        return Response(serializer.data)

class ProfesorList(APIView):
    
    def get(self, request, format=None):
        queryset =  Profesor.objects.filter(status=0)
        serializer = ProfesorSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = ProfesorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
