from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)

class Kitty(models.Model):
    color = models.CharField(max_length=100)
