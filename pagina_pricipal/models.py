from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.urls import reverse

    

class Palestra(models.Model):
    name = models.CharField(max_length=200, null= True, blank=True, verbose_name="Nome")
    link = models.CharField(max_length=1000, null= True, blank=True)
                            

    def __str__(self):
        return self.link


    class Meta:
        verbose_name = 'Link Palestra Principal'

class Workshop(models.Model):
    name = models.CharField(max_length=200, null= True, blank=True, verbose_name="Nome")
    link = models.CharField(max_length=1000, null= True, blank=True)

    def __str__(self):
        return self.name



