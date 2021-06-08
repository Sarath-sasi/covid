from django.db import models

# Create your models here.

class NewClass(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class FormClass(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    text = models.CharField(max_length=50)

class csClass(models.Model):
    name = models.CharField(max_length=255)
    eml = models.CharField(max_length=300)
    sbt = models.CharField(max_length=200)
    mess = models.CharField(max_length=200)

