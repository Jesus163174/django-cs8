from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404


from sucursal.models import Sucursal
from sucursal.serializers import SucursalSerializer

class SucursalList(APIView):
    
    def get(self, request, format=None):
        queryset = Sucursal.objects.filter(status=0)
        serializer = SucursalSerializer(queryset, many=True)
        return Response(serializer.data)
    
    '''def post(self, request, format=None):
        serializer = SucursalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)'''

class SucursalDetail(APIView):
    def get_object(self, id):
        try:
            return Sucursal.objects.get(pk=id)
        except Sucursal.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SucursalSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)