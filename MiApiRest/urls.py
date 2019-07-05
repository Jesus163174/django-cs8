from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/v1/login', include('login.urls')),
    re_path(r'^api/v1/',include('servicio.urls')),
    re_path(r'^api/v1/',include('perfil.urls')),
    re_path(r'^api/v1/',include('empleado.urls')),
    re_path(r'^api/v1/',include('alumno.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)