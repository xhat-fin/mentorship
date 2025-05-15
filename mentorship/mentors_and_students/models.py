from django.db import models

# Create your models here.


class Mentor(models.Model):
    name = models.CharField(max_length=150)
    sphere = models.TextField()
    experience = models.TextField()


class Student(models.Model):
    name = models.CharField(max_length=150)
    descriptions = models.TextField()
