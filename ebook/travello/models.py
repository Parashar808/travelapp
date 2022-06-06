from django.db import models

class Destination(models.Model):
    
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    des=models.TextField()
    price=models.IntegerField()
    video=models.FileField(upload_to='vids')

# Create your models here.
    