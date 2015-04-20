from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .meteo import get_meteo

def index(request):
    return HttpResponse(get_meteo())