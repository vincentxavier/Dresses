# -*- coding: utf8 -*-
# Créé par jumelvin, le 22/01/2015 en Python 3.2

import urllib, json, datetime, urllib2

key='b05da061-a7fe-43b1-ba6b-8bf247357d78'

def query_navitia(api_call=''):
    """Fonction d'appel de l'api"""
    api_call = urllib.quote(api_call, safe='/?=&,')
    url = 'https://api.navitia.io/' + 'v1/coverage/fr-idf' + api_call
    req = urllib2.Request(url)
    req.add_header('Authorization', key)
    response = urllib2.urlopen(req)
    return json.loads(response.read().decode().strip())


def get_journeys():
    """Fonction pour renvoyer les trajets possibles"""

    addresse_depart = query_navitia('/places?q=4 passage Lacroix, Saint-Denis')
    addresse_arrivee = query_navitia('/places?q=15 route des gardes, Meudon')

    #arret_depart = query_navitia('/coords/'+addresse_depart['places'][0]['id']+'/places_nearby')
    #arret_arrivee = query_navitia('/coords/'+addresse_arrivee['places'][0]['id']+'/places_nearby')

    date = datetime.datetime.now()

    journey_call = "/journeys?from={resource_id_1}&to={resource_id_2}&datetime={datetime}".format(
        resource_id_1=addresse_depart['places'][0]['id'],
        resource_id_2=addresse_arrivee['places'][0]['id'],
        datetime=date.strftime('%Y%m%dT%H%M'))
    return query_navitia(journey_call)


def get_best_route(journey):
    """Renvoie la meilleure des routes (au sens de navitia)"""
    routes = journey['journeys']
    for route in routes:
        if route['type'] == 'best':
            best_route = route
    return best_route


def poi_departs_arrivees(best_route):
    """Renvoie les points d'arrivées et de départ"""
    departs = []
    arrivees = []
    for section in best_route['sections']:
        if section['type'] != 'waiting':
            departs.append(section['geojson']['coordinates'][0])
            arrivees.append(section['geojson']['coordinates'][-1])
    return departs, arrivees


def get_lines(best_route):
    """Renvoie les parties des la route"""
    lines = {}
    i = 0
    for section in best_route['sections']:
        i += 1
        line = []
        if section['type'] != 'waiting':
            for coord in section['geojson']['coordinates']:
                line.append([coord[1], coord[0]])
            lines[i] = line
    return lines


def get_poi_departs(departs):
    """Donne les points de départs en les inversant pour leaflet"""
    poi_departs = {}
    poi_num = 0
    for i in departs:
        poi_num += 1
        poi_departs[poi_num] = [i[1], i[0]]
    return poi_departs


TRAJET = get_journeys()
MEILLEUR_TRAJET = get_best_route(TRAJET)
#departs, arrivees = poi_departs_arrivees(meilleur_trajet)

print(get_lines(MEILLEUR_TRAJET))
