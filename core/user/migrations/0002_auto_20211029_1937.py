# Generated by Django 3.0.4 on 2021-10-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='curp',
            field=models.CharField(blank=True, max_length=18, verbose_name='CURP'),
        ),
    ]
