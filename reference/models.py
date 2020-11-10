from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

# class Referencias(models.Model):
#     referencias = models.TextField(blank=True)
    

class Trabalhos(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)
    data_criacao = models.DateField()
    # referencias = models.ManyToManyField(Referencias)
    referencias = ArrayField(models.TextField(null=True, blank=True))

