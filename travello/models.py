from xmlrpc.client import boolean
from django.db import models

# Create your models here.
class Destination:
    id :int
    name: str
    img:str
    description:str
    price:int
    offer:boolean
