from crum import get_current_user
from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import sexo_choices, edo_civil_choices, gender_choices
from core.models import BaseModel


# from smart_selects.db_fields import ChainedForeignKey

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


class Persona(models.Model):
    curp = models.CharField(max_length=18, blank=True, unique=True, verbose_name='CURP')
    nombre = models.CharField(max_length=25, verbose_name='Nombre')
    apaterno = models.CharField(max_length=25, verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=25, verbose_name='Apellido Materno')
    image = models.ImageField(upload_to='alumnos/%Y/%m/%d', null=True, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name='Fechas de Nacimiento')
    lugar_nacimiento = models.CharField(max_length=255, blank=True, null=True, verbose_name='Lugar de Nacimiento')
    rfc = models.CharField(max_length=13, blank=True, verbose_name='RFC')
    edo_civil = models.CharField(max_length=30, choices=edo_civil_choices, default='S', verbose_name='Estado Civil')
    sexo = models.CharField(max_length=10, choices=sexo_choices, default='male', verbose_name='Sexo')
    domicilio = models.CharField(max_length=255, blank=True, null=True, verbose_name='Domicilio')
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True)

    calle = models.TextField(max_length=40, blank=True, null=True, verbose_name='Calle')
    no = models.CharField(max_length=5, blank=True, verbose_name='Número')
    no_int = models.CharField(max_length=5, blank=True, verbose_name='Número Int.')
    lic_conducir = models.CharField(max_length=25, blank=True, verbose_name='Licencia de conducir')
    tel_casa = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono de casa')
    tel_cel = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefono celular')
    escolaridad = models.CharField(max_length=255, blank=True, verbose_name='Escolaridad')

    def __str__(self):
        return self.nombre

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ['-id']


class Curso(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Persona')
    curso = models.CharField(max_length=100, unique=True, verbose_name='Curso')
    categoria = models.CharField(max_length=50, blank=True, null=True, verbose_name='Categoria')
    descripcion = models.TextField(max_length=50, blank=True, null=True, verbose_name='Descripción')

    def __str__(self):
        return self.curso

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Curso, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = self.get_gender_display()
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']