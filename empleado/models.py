from django.db import models

class Negocio(models.Model):
    name   = models.CharField(max_length=50, blank=True)
    state  = models.CharField(max_length=50, blank=True)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = 'negocios'
        
class Empleado(models.Model):
    name   = models.CharField(max_length=50, blank=True)
    state  = models.CharField(max_length=50, blank=True)
    negocio = models.ForeignKey(Negocio, related_name='empleados', on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = 'empleados'
