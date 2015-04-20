import urllib, json, datetime

# http://api.openweathermap.org/data/2.5/forecast/daily?q=Saint-Denis&mode=xml&units=metric&cnt=7

def get_meteo():
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?' + 'APPID=cde53cf818696b0d5a4bdaf6999d3fb0' \
    + '&id=2980916'+'&units=metric'+'cnt=1'
    meteo = json.loads(urllib.urlopen(url).read().decode().strip())

    temperatures = meteo['list'][0]['temp']

    temp_jour = temperatures['day'] - 273.15
    temp_soir = temperatures['eve'] - 273.15
    temp_max = temperatures['max'] - 273.15
    temp_min = temperatures['min'] - 273.15
    temp_matin = temperatures['morn'] - 273.15
    temp_nuit = temperatures['night'] - 273.15

    humidite = meteo['list'][0]['humidity']
    vitesse_vent = meteo['list'][0]['speed']
    direction_vent = meteo['list'][0]['deg']
    etat_ciel = meteo['list'][0]['weather'][0]['main']
    
    return {'jour': temp_jour, 'soir': temp_soir, 'max': temp_max, 'min': temp_min, 'matin': temp_matin, 'nuit': temp_nuit}

print(get_meteo())