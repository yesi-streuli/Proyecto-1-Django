# Generated by Django 3.0.9 on 2020-08-13 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
