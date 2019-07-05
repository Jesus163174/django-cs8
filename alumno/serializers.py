from rest_framework import routers, serializers, viewsets
from alumno.models import Alumno
from alumno.models import Profesor



class AlumnoSerializer(serializers.ModelSerializer):
    profesores = serializers.PrimaryKeyRelatedField(queryset=Profesor.objects.all(), many=True)
    class Meta:
        model = Alumno
        fields = ('name','matricula')
class ProfesorSerializer(serializers.ModelSerializer):
    Profesor_list = AlumnoSerializer(many=True, read_only=True)
    class Meta:
        model = Profesor
        fields = ('name','profesor_list','completo','salario')
