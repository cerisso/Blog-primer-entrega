from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100, unique=True)
    contrasenia = models.CharField(max_length=400)
    def __str__(self):
        return (f"User: {self.nombre_usuario}, password: {self.contrasenia}")

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=30)
    def __str__(self):
        return (f"categoria: {self.categoria}")

class Posteos(models.Model):
    id = models.AutoField(primary_key=True)
    contenido = models.CharField(max_length=4000)
    fecha_hora = models.DateTimeField(auto_now_add=True) 
    autor = models.CharField(max_length=100)
    def __str__(self):
        return (f"id: {self.id}, autor: {self.autor}, fecha_hora: {self.fecha_hora}")