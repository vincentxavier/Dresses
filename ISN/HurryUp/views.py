from django.shortcuts import render

# Create your views here.


def index(request):
    """Construction de l'index a partir des fonctions crees ailleurs"""
    context=None
    return render(request,"HurryUp/index.html",context)