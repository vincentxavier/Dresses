from django.shortcuts import render

# Create your views here.
from .journeys import *

def index(request):
    """Construction de l'index a partir des fonctions crees ailleurs"""
    journey = get_journeys()
    best_route = get_best_route(journey)
    departs, arrivees = poi_departs_arrivees(best_route)
    poi_departs = get_poi_departs(departs)
    context = {
        'poi_departs': poi_departs,
    }
    return render(request,"HurryUp/index.html",context)