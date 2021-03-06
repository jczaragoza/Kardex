<<<<<<< HEAD
# Generated by Django 3.0.4 on 2021-10-29 23:57
=======
# Generated by Django 3.0.4 on 2021-11-04 18:24
>>>>>>> 9afd8781dfd6dea898757abe22a8f66b9f2770cf

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('curp', models.CharField(blank=True, max_length=18, unique=True, verbose_name='CURP')),
                ('secon_name', models.CharField(max_length=25, verbose_name='Apellido Materno')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fechas de Nacimiento')),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Lugar de Nacimiento')),
                ('rfc', models.CharField(blank=True, max_length=13, verbose_name='RFC')),
                ('edo_civil', models.CharField(choices=[('S', 'Soltero(a)'), ('M', 'Casado(a)'), ('U', 'Uni??n libre'), ('D', 'Divorciado(a) y/o Separado(a)')], default='S', max_length=1)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('domicilio', models.CharField(blank=True, max_length=255, null=True, verbose_name='Domicilio')),
                ('calle', models.TextField(blank=True, max_length=40, null=True, verbose_name='Calle')),
                ('no', models.CharField(blank=True, max_length=5, verbose_name='N??mero')),
                ('no_int', models.CharField(blank=True, max_length=5, verbose_name='N??mero Int.')),
                ('lic_conducir', models.CharField(blank=True, max_length=25, verbose_name='Licencia de conducir')),
                ('tel_casa', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tel??fono de casa')),
                ('tel_cel', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono celular')),
                ('nacionalidad', models.CharField(choices=[('M', 'Mexicano'), ('E', 'Extranjero')], default='M', max_length=1)),
                ('escolaridad', models.CharField(blank=True, max_length=255, verbose_name='Escolaridad')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Estado', verbose_name='Estado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Municipio', verbose_name='Municipio')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
