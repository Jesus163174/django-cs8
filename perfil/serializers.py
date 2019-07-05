from rest_framework import routers, serializers, viewsets
from perfil.models import Perfil
from perfil.models import Sex
from perfil.models import City

class PerfilSerializer(serializers.ModelSerializer):
    nameCity = serializers.ReadOnlyField(source='city.name')
    stateCity = serializers.ReadOnlyField(source='city.state')
    nameSex  = serializers.ReadOnlyField(source='sex.name')
    class Meta:
        model = Perfil
        fields = ('__all__')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')

class SexSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Sex
        fields = ('__all__')