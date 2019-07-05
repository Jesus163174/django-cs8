from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404


from perfil.models import Perfil
from perfil.serializers import PerfilSerializer


class Profile(APIView):
    def get_object(self, id):
        try:
            return Perfil.objects.get(user=id)
        except Perfil.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = PerfilSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
