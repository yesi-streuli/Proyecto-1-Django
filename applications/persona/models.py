from django.db import models
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('HABILIDAD', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad
        
        

#Create your models here.

class Persona(models.Model):
    """Modelo para tabla Persona"""

    Job_Choices = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    first_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField("Trabajo", max_length=1, choices=Job_Choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = ' Mi Empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name