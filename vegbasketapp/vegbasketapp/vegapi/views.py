from django.shortcuts import render
from haystack.query import SearchQuerySet
from haystack.utils.geo import Point, D
lat = 2.1941695
long = 41.3892221


def get_closest(request, long, lat):
    ninth_and_mass = Point(long, lat)
    max_dist = D(mi=20)
    sqs = SearchQuerySet().dwithin('location', ninth_and_mass, max_dist)
    
    result.model
result.object
result.object
result.object
result.object.long
result.object.lat
history
