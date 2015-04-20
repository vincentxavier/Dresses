from django.shortcuts import render

# Create your views here.
from .models import Vetement
from .meteo import get_meteo

def index(request):
    """Construction de l'index a partir des fonctions crees ailleurs"""
    temperature = get_meteo()
    vetements = Vetement.objects.filter(temp_min__lte=temperature['min']).filter(temp_max__gte=temperature['max'])
    context = {
        'temperature': temperature,
        'vetements': vetements,
    }
    return render(request,"dresses/index.html",context)
