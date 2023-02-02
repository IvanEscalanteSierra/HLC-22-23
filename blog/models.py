from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()


class Articulos(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def crear_articulo(p_nombre, p_seccion, p_precio):
        art =  Articulos.objects.create(nombre=p_nombre, seccion=p_seccion, precio=p_precio)
        art.save()
        return art

    def todos_los_articulos():
        todos = Articulos.objects.all()
        return todos

    def borrar_articulo(p_id):
        Articulos.objects.get(id=p_id).delete()

    def update_articulo(p_id,p_nombre,p_seccion,p_precio):
        art = Articulos.objects.get(id=p_id)
        art.nombre = p_nombre
        art.seccion = p_seccion
        art.precio = p_precio
        art.save
        return art

    def __str__(self):
        return '{} y su precio es {}'.format(self.nombre,self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    entregado = models.BooleanField()
