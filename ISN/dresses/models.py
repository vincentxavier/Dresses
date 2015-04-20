from django.db import models

# Create your models here.

models.Field.default = False
class Vetement(models.Model):
    nom = models.CharField(max_length=200)
    temp_max = models.IntegerField()
    temp_min = models.IntegerField()
    pluie = models.BooleanField()