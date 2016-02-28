from django.shortcuts import render, redirect, HttpResponse

from vegbasketapp.transformer.tools_entry import get_entry_by_id, \
     get_reviews_by_entry_id, get_region_by_id, get_entry_geo

def entry_map(request, entry_id):
    entry = get_entry_by_id(entry_id)
    try:
        cords = get_entry_geo(entry)
    except IndexError:
        return render(request, "entry_map.html")
        #return HttpResponse('')
    cords['c1lng'] = cords['lng']+0.01
    cords['c2lng'] = cords['lng']-0.01
    cords['c1lat'] = cords['lat']+0.01
    cords['c2lat'] = cords['lat']-0.01
    return render(request, "entry_map.html", {'cords':cords, 'name':entry.get_elem('name')})

def entry(request, entry_id):
    force = request.GET.get('force', False)
    entry_tmp = get_entry_by_id(entry_id, force)
    entry_tmp.set_obj()
    return HttpResponse(entry_tmp.results_source)

def entry_reviews(request, entry_id):
    entry_reviews_tmp = get_reviews_by_entry_id(entry_id)
    return HttpResponse(entry_reviews_tmp.results_source)

def region(request, region_id):
    force = request.GET.get('force', False)
    region_tmp = get_region_by_id(region_id, force)
    return HttpResponse(region_tmp.results_source)

def region_root(request, region_id):
    force = request.GET.get('force', False)
    region_tmp = get_region_by_id(0, force)
    return HttpResponse(region_tmp.results_source)
