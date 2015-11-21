from urllib import request
from urllib.parse   import quote
import json
import datetime
import re
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from vegbasketapp.transformer.vegguide import VegGuideObject, VegGuideObjectEntries
from vegbasketapp.transformer.models import Entry, Region, Reviews
from django.utils import timezone

regex_region = re.compile(r'http.*region/(\d*)')
regex_entry = re.compile(r'http.*entry/(\d*)')

def is_cached_region(source_id):
    return True if Region.objects.filter(source_id=source_id).count() > 0 else False 


def get_region(uri, force=False):
    source_id = regex_region.findall(uri)[0]
    return get_region_by_id(source_id)

def fetch_region(source_id, force=False):
    vgo = VegGuideObject('http://www.vegguide.org/region/%s' % source_id)
    region, created = Region.objects.update_or_create(source_id=source_id,
        defaults={'results_source':vgo.results_json, 
        'modified_source':timezone.now()})
    # region = Region(source_id=source_id)

    
    # region.results_source = vgo.results_json
    # region.modified_source = 
    # region.save()
    return region    


def get_region_by_id(source_id, force=False):
    if force or Region.objects.filter(source_id=source_id,
                                      modified__gte=datetime.datetime.now()-datetime.timedelta(
                                          days=settings.DEFALT_EXPIRE_TIME)).count()==0:
        region = fetch_region(source_id, force)
    else:
        region = Region.objects.get(source_id=source_id)
        
    #print (region.modified_source)
    return region


def get_entry(uri, force=False):
    source_id = regex_entry.findall(uri)[0]
    return(get_entry_by_id(source_id), force)

def fetch_entry(source_id, force=False):
    vgo = VegGuideObject('http://www.vegguide.org/entry/%s' % source_id)
    obj = json.loads(vgo.results_json)
    region_uri = obj['region']['uri']
    
    #try:
        #region_uri = obj['region']['uri']
    #except KeyError:
        #from ipdb import set_trace; set_trace()
    region = get_region(region_uri, force)

    entry, created = Entry.objects.update_or_create(source_id=source_id,
        defaults={'region':region, 'results_source':vgo.results_json,
        'modified_source':timezone.now()})
    entry.save()
    return entry

def get_entry_by_id(source_id, force=False):
    if force or Entry.objects.filter(source_id=source_id,
                                     modified__gte=datetime.datetime.now()-datetime.timedelta(
                                         days=settings.DEFALT_EXPIRE_TIME)).count()==0:
        entry = fetch_entry(source_id)
    else:
        entry = Entry.objects.get(source_id=source_id)
        
        
    #print (entry.modified)
        
    return entry

def get_reviews_by_entry_id(source_id):
    try:
        reviews = Reviews.objects.get(source_id=source_id)
    except ObjectDoesNotExist:
        entry = get_entry_by_id(source_id)
        reviews = Reviews(source_id=source_id,entry=entry)
        vgo = VegGuideObject('http://www.vegguide.org/entry/%s/reviews' % source_id)
        reviews.results_source = vgo.results_json
        reviews.modified_source = timezone.now()
        reviews.save()
    return reviews

geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"
geocode_place_url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s"

def get_entry_geo(entry):
    obj = json.loads(entry.results_source)
    address_prepared = quote(entry.get_address_str().replace(' ', '+'))
    if not entry.results_geo:
        url = geocode_url % (address_prepared, settings.GOOGLE_GEOCODE_API_KEY)
        req = request.urlopen(url)
        data = req.readall().decode('utf-8')
        result = data
        entry.results_geo = result
        entry.save()


        entry.set_obj_geo()
        location = entry.obj_geo['results'][0]
        if 'place_id' in location:
            place_id = location['place_id']
            url = geocode_place_url % (place_id, settings.GOOGLE_GEOCODE_API_KEY)
            req = request.urlopen(url)
            data = req.readall().decode('utf-8')
            entry.results_geo_place = data
            entry.save()
    return entry.get_cord()


def get_entries(url):
    entries = VegGuideObjectEntries(url)
    #print(entries)
    return entries