from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=59)
    edad=models.IntegerField()
    fecha_nac=models.DateField()

    