from django.db import models

# Create your models here.
class Item(models.Model):
    nom=models.CharField(max_length=25)
    email=models.EmailField(max_length=100)
    mdp=models.CharField(('password'), max_length=9)
    