from distutils.command.upload import upload
from sys import maxsize
from xmlrpc.client import boolean
from django.db import models

# Create your models here.
class Destination(models.Model):
    name =  models.CharField(max_length=100)
    img =models.ImageField(upload_to = 'static/imgs/place')
    price =models.IntegerField()
    offer = models.BooleanField(default = False)
    descr = models.TextField()
