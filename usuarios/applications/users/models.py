from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    USERNAME_FIELD = 'username'

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombre + ' ' + self.apellido