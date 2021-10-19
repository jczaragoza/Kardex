from django.db import models
from datetime import datetime
from django.forms import model_to_dict
#from smart_selects.db_fields import ChainedForeignKey

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
    #foto = models.ImageField(blank=True, null=True, upload_to='persona/fotos')
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
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True)

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
    correo = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Correo')
    escolaridad = models.CharField(max_length=255, blank=True, verbose_name='Escolaridad' )
    #f_registo= models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    #f_modificado  = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        ordering = ['-id']

class Curso(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    curso = models.CharField(max_length=255, null=True, blank=True)
    tipo_curso = models.CharField(max_length=100, blank=True, null=True)
    fecha_curso = models.DateField(blank=True, null=True)
    duracion = models.DateField(blank=True, null=True)
    documento = models.DateField(blank=True, null=True)
