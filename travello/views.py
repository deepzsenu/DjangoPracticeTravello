# Create your views here.

from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from travello.models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.price = 700
    dest1.name = "Mumbai"
    dest1.img = '/static/place/1.png'
    dest1.description = "the city where people never sleeps"

    dest2 = Destination()
    dest2.price = 6500
    dest2.name = "Delhi"
    dest2.img = '/static/place/2.png'
    dest2.description = "The city where peoples struggles"


    dest3= Destination()
    dest3.price = 800
    dest3.name = "Bangalore"
    dest3.img = '3.png'
    dest3.description = "The IT hub of India and a lot of job fraud"

    return render(request, "index.html",{'dest1':dest1,'dest2':dest2, 'dest3':dest3})
