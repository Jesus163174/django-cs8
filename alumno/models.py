from django.db import models

class Profesor(models.Model):
    name = models.CharField(null=False, max_length=100)
    completo = models.BooleanField(null=False)
    salario  = models.DecimalField(max_digits=5, decimal_places=2,null=False)
    date_joined = models.DateField(null = False)

    class Meta:
        db_table = "profesores"

class Alumno(models.Model):
    name = models.CharField(null=False, max_length=100)
    matricula = models.CharField(null=False, max_length=6)
    curp = models.CharField(null=False, max_length=15)
    telefono = models.CharField(null = True, max_length=10)
    date_joined = models.DateField(null = False)
    profesores = models.ManyToManyField(Profesor, related_name="profesor_list", blank=True)

    class Meta:
        db_table = "alumnos"
