from django.shortcuts import render
from haystack.query import SearchQuerySet
from haystack.utils.geo import Point, D
from django.http import HttpResponse

import json


def get_closest(request):
    
    print(request.GET)
    long = float(request.GET.get('long',0))
    lat = float(request.GET.get('lat',0))
    ninth_and_mass = Point(long, lat)
    max_dist = D(mi=20)
    sqs = SearchQuerySet().dwithin('location', ninth_and_mass, max_dist)
    
    data = {'counter':0 ,'places':[]}
    

    if sqs.count()==0:
        return HttpResponse(content=json.dumps(data))
    
    
    
    for elem in sqs.all():
        data['counter'] += 1
        place = {'long':0, 'lat':0, 'title':''}
        place['long'] = float(elem.object.long)
        place['lat'] = float(elem.object.lat)
        place['title'] = elem.object.name
        place['level'] = elem.object.level
        data['places'].append(place)
    return HttpResponse(content=json.dumps(data))
        

