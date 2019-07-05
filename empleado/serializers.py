from rest_framework import routers, serializers, viewsets
from empleado.models import Negocio
from empleado.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    #nameSucursal = serializers.ReadOnlyField(source='sucursal.name')
    class Meta:
        model = Empleado
        fields = ('name')

class NegocioSerializer(serializers.ModelSerializer):
    empleados = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Negocio
        fields = ('name','empleados')
