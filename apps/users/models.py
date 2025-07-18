from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.empresa.models import Empresa

# Create your models here.

SEXO = (("M","Masculino"),("F","Femenino"))


class User(AbstractUser):
    empresa = models.ForeignKey(Empresa, null = True, blank=True, on_delete = models.CASCADE)
    cargo = models.CharField(null=True, blank=True, max_length=30)
    edad = models.IntegerField(null=True, blank=True)
    sexo = models.CharField(null=True, blank=True, max_length=11, choices=SEXO)
    is_admin = models.BooleanField('Is admin',default=False)
    is_normal = models.BooleanField('Is normal',default=False)
    aprobado = models.BooleanField('Aprove', default=False)
