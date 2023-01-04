import datetime
from django.db import models

class Docente(models.Model):
    codigo=models.CharField(max_length=6,primary_key=True)
    nombre=models.CharField(max_length=20)
    apellido_paterno=models.CharField(max_length=20)
    apellido_materno=models.CharField(max_length=20)
    dni=models.CharField(max_length=8)
    fecha_nacimiento=models.DateTimeField('Fecha de nacimiento')
    fecha_registro=models.DateTimeField(datetime.datetime.now())
    estado=models.CharField(max_length=10)
