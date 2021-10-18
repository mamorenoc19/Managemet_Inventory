from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    etiqueta = models.CharField(max_length=30)
    cantidad = models.IntegerField()

    def nombre_vista_producto(self):
        #nombre,marca,cantidad
        cadena = '{0}, {1}, {2}'
        return cadena.format(self.nombre, self.marca, self.cantidad)

    def __str__(self):
        return self.nombre_vista_producto()
