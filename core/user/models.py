from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict
from datetime import datetime

from config.settings import MEDIA_URL, STATIC_URL


class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Colonia(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class User(AbstractUser):
    curp = models.CharField(max_length=18, blank=True, verbose_name='CURP')
    secon_name = models.CharField(max_length=25, verbose_name='Apellido Materno')
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name='Fechas de Nacimiento')
    lugar_nacimiento = models.CharField(max_length=255, blank=True, null=True, verbose_name='Lugar de Nacimiento')
    rfc = models.CharField(max_length=13, blank=True, verbose_name='RFC')
    edo_civil_com = [
        ('S', 'Soltero(a)'),
        ('M', 'Casado(a)'),
        ('U', 'Unión libre'),
        ('D', 'Divorciado(a) y/o Separado(a)')
    ]

    edo_civil = models.CharField(max_length=1, choices=edo_civil_com, default='S')
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    domicilio = models.CharField(max_length=255, blank=True, null=True, verbose_name='Domicilio')
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Estado')
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Municipio')
    calle = models.TextField(max_length=40, blank=True, null=True, verbose_name='Calle')
    no = models.CharField(max_length=5, blank=True, verbose_name='Número')
    no_int = models.CharField(max_length=5, blank=True, verbose_name='Número Int.')
    lic_conducir = models.CharField(max_length=25, blank=True, verbose_name='Licencia de conducir')
    tel_casa = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono de casa')
    tel_cel = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefono celular')
    nacionalida_com = [
        ('M', 'Mexicano'),
        ('E', 'Extranjero')
    ]
    nacionalidad = models.CharField(max_length=1, choices=nacionalida_com, default='M')
    escolaridad = models.CharField(max_length=255, blank=True, verbose_name='Escolaridad')


    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ['-id']
