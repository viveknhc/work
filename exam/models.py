from django.db import models

# Create your models here.
class Registration(models.Model): 
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Exam(models.Model):
    title =models.CharField(max_length=30)


class Question(models.Model):
    titles =models.CharField(max_length=30)
    qstn =models.CharField(max_length=30)
    opt1 =models.CharField(max_length=30)
    opt2 =models.CharField(max_length=30)
    opt3 =models.CharField(max_length=30)
    opt4 =models.CharField(max_length=30)
    mark =models.CharField(max_length=30)
    answer =models.CharField(max_length=30)