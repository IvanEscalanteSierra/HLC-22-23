from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    telefono= models.IntegerField()


class Articulos(models.Model):
    nombre= models.CharField(max_length=50, null=True)
    sección= models.CharField(max_length=50)
    precio= models.IntegerField()


class Pedidos(models.Model):
    numero= models.IntegerField()
    entregado= models.BooleanField()
