from django.db import models

class Sucursal(models.Model):
    name    = models.CharField(max_length=50, blank=True)
    address = models.TextField(max_length=50, blank=True)
    number  = models.IntegerField(null=False)
    status  = models.BooleanField(default= True)
    class Meta:
        db_table = "sucursal"

class Product(models.Model):

    name  = models.CharField(max_length=50, blank=True)
    stock = models.IntegerField(null=False)
    sucursal = models.ForeignKey(Sucursal, related_name='products', on_delete=models.CASCADE)
    costo    = models.DecimalField(max_digits=5, decimal_places=2,null=False)
    precio   = models.DecimalField(max_digits=5, decimal_places=2,null=False)

    class Meta:
        db_table = "products"