from django.db import models
# from sqlalchemy import false

class Destination(models.Model):
    
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    des=models.TextField()
    price=models.IntegerField()
    duration=models.CharField(max_length=100)
    des1=models.TextField(null='True',default='no defined')    

# Create your models here.
