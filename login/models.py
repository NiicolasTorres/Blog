from email.policy import default
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='Morgoth.jpg')

    def __str__(self):
        return f'Perfil de{self.user.username}'



