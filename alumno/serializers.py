from rest_framework import routers, serializers, viewsets
from alumno.models import Alumno
from alumno.models import Profesor



class AlumnoSerializer(serializers.ModelSerializer):
    #profesores = serializers.PrimaryKeyRelatedField(queryset=Profesor.objects.all(), many=True)
    profesores = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Alumno
        fields = ('__all__')
class ProfesorSerializer(serializers.ModelSerializer):
    alumnos_list = AlumnoSerializer(many=True, read_only=True)
    class Meta:
        model = Profesor
        fields = ('__all__')
