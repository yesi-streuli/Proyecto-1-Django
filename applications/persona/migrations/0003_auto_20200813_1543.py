# Generated by Django 3.0.9 on 2020-08-13 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20200813_1537'),
        ('persona', '0002_auto_20200813_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['-first_name', 'last_name'], 'verbose_name': ' Mi Empleado', 'verbose_name_plural': 'Empleados de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('first_name', 'departamento')},
        ),
    ]
