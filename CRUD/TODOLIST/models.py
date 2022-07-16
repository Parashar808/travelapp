from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
   

class Complain(models.Model):
    CompId = models.CharField(max_length=10)
    Name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=10)
    Email = models.EmailField()
    Description = models.CharField(max_length=1000)
    class Meta:
        db_table="CRUD"


    