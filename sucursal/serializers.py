from rest_framework import routers, serializers, viewsets
from sucursal.models import Sucursal
from sucursal.models import Product

class ProductSerializer(serializers.ModelSerializer):
    #nameSucursal = serializers.ReadOnlyField(source='sucursal.name')
    class Meta:
        model = Product
        fields = ('name')

class SucursalSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Sucursal
        fields = ('name','products')
    
    






