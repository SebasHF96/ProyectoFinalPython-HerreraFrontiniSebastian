from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    def __str__(self):
        return f"User: {self.user} - email: {self.email}"
    user = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=20)    

class Producto(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - sku: {self.sku}"
    nombre = models.CharField(max_length=30)
    sku = models.IntegerField()
    marca = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)    

class Proveedor(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - email: {self.email}"
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    email = models.CharField(max_length=40)   

class Cliente(models.Model):
    def __str__(self):
        return f"Cliente: {self.cliente} - email: {self.email}"
    cliente = models.CharField(max_length=15)
    telefono = models.IntegerField()
    email = models.CharField(max_length=20)

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


