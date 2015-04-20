from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

from .meteo import get_meteo

def index(request):
    temperature = get_meteo()
    template = loader.get_template('dresses/index.html')
    context = RequestContext(request, {
        'temperature': temperature,
    })
    return HttpResponse(template.render(context))