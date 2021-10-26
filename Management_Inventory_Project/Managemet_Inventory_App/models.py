from django.db import models
from django.forms import ModelForm

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

class Categorias(models.Model):
    lista_categoria = [(1,'Carnes y embutidos'), (2,'Frutas y Verduras'), (3,'Panadería y dulces'), (4,'Huevos, lacteos y café'), (5,'Aceites y pastas'),(6,'Conservas y comida preparada'), (7,'Zumos y bebidas'), (8,'Aperitivos'), (9,'Cosmética y cuidado personal'), (10,'Hogar y limpieza'), (11,'Ropa')]
    categoría = models.CharField(max_length=1, choices=lista_categoria, default=1)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

class producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)
    marca= models.CharField(max_length=30)
    sede = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    proveedor = models.CharField(max_length=30)
