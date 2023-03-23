from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    profile_pic = models.ImageField(
        upload_to='images/profiles_pic', null=True, blank=True)
