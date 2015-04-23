from django.shortcuts import render

def index(request):
    """Affiche une page d'accueil"""
    projets = {'dresses': 'Jade et Wendy'}
    context = {'projets' : projets}
    return render(request,"index.html",context)
