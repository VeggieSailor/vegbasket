from django.shortcuts import render
#from vegbasketapp.transformer.models import Entry, Region, Review
from vegbasketapp.transformer.tools_entry import get_entry_by_id, \
	get_reviews_by_entry_id, get_region_by_id, get_entry_geo
from django.http import HttpResponse

# Create your views here.

def entry_map(request, entry_id):
	entry = get_entry_by_id(entry_id)
	cords = get_entry_geo(entry)
	cords['c1lng'] = cords['lng']+0.01
	cords['c2lng'] = cords['lng']-0.01
	cords['c1lat'] = cords['lat']+0.01
	cords['c2lat'] = cords['lat']-0.01
	return render(request, "entry_map.html", {'cords':cords})

def entry(request, entry_id):
	print(entry_id)
	entry_tmp = get_entry_by_id(entry_id)
	return HttpResponse(entry_tmp.results_source)

def entry_reviews(request, entry_id):
	entry_reviews_tmp = get_reviews_by_entry_id(entry_id)
	return HttpResponse(entry_reviews_tmp.results_source)


def region(request, region_id):
	region_tmp = get_region_by_id(region_id)	
	return HttpResponse(region_tmp.results_source)