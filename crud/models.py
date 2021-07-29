from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    nim = models.TextField()
    name = models.TextField()
    email = models.EmailField()

class Task(models.Model):
    first = models.TextField()
    second = models.TextField()
    res = models.TextField()