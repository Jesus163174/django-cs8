

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404


from empleado.models import Empleado
from empleado.serializers import EmpleadoSerializer

from empleado.models import Negocio
from empleado.serializers import NegocioSerializer

class NegociosList(APIView):
    
    def get(self, request, format=None):
        queryset = Negocio.objects.filter(status=0)
        serializer = NegocioSerializer(queryset, many=True)
        return Response(serializer.data)

class NegocioDetail(APIView):
    def get_object(self, id):
        try:
            return Negocio.objects.get(pk=id)
        except Negocio.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = NegocioSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EmpleadosList(APIView):

    def get(self, request, format=None):
        queryset = Empleado.objects.filter(status=0)
        serializer = EmpleadoSerializer(queryset, many=True)
        return Response(serializer.data)

