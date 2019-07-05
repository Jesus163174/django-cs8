from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name   = models.CharField(max_length=50, blank=True)
    state  = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=True)
    colony = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = "cities"

class Sex(models.Model):

    name = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = "sexs"

class Perfil(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day   = models.DateField(null=True, blank=True)
    adress      = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=1000 , blank=True)
    created_at  = models.DateField(null=True, blank=True)
    city        = models.OneToOneField(City , on_delete=models.CASCADE)
    phone       = models.CharField(max_length=10, null=False)
    sex         = models.OneToOneField(Sex, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='media/', null=True)

    class Meta:
        db_table = "Profile"


    

