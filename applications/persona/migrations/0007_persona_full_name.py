# Generated by Django 3.0.9 on 2020-08-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_persona_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres completos'),
        ),
    ]