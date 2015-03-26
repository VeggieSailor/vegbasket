from django.shortcuts import render
from vegbasketapp.transformer.models import Entry, Region
from vegbasketapp.transformer.tools_entry import get_entry_by_id,get_entry_geo

# Create your views here.

def entry_map(request, entry_id):

	try:
		entry = get_entry_by_id(entry_id)
		cords = get_entry_geo(entry)
		cords['c1lng'] = cords['lng']+0.01
		cords['c2lng'] = cords['lng']-0.01
		cords['c1lat'] = cords['lat']+0.01
		cords['c2lat'] = cords['lat']-0.01
		return render(request, "entry_map.html", {'cords':cords})
	except:
		return render(request, "entry_map_error.html")
