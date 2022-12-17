from django.db import models

# Create your models here.


class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=40)
    fecha_alta = models.DateField()


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    codigo = models.IntegerField()
