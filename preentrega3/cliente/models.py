from django.db import models

# Create your models here.

class Pais(models.Model):       #models es un modulo y Model es la clase  no se puede heredar un modulo sino clases
     nombre = models.CharField(max_length=100)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)   
    
    apellido = models.CharField(max_length=100)
    
    nacimiento =models.DateField(null =True, blank =True) # trabaja con la base de datos y con lo que se de en ls vistas (template)
    
    pais_origen_id = models.ForeignKey(Pais,null=True,blank=True,on_delete=models.SET_NULL)#necesita como argumento el modelo al qeu hace referencia
    
    
    
    