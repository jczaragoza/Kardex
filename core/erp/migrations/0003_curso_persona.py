# Generated by Django 3.0.4 on 2021-10-30 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20211029_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.Persona', verbose_name='Persona'),
        ),
    ]