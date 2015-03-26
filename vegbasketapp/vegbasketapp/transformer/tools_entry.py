from django.core.exceptions import ObjectDoesNotExist
from vegbasketapp.transformer.vegguide import VegGuideObject
from vegbasketapp.transformer.models import Entry, Region


import datetime
import re
from django.conf import settings
regex_region = re.compile(r'http.*region/(\d*)')
regex_entry = re.compile(r'http.*entry/(\d*)')

from urllib import request

import json

def get_region(uri):
    source_id = regex_region.findall(uri)[0]
    try:
        region = Region.objects.get(source_id=source_id)
    except ObjectDoesNotExist:
        print("no region")
        region = Region(source_id=source_id)
        vgo = VegGuideObject(uri)
        region.results_source = vgo.results_json
        region.modified_source = datetime.datetime.now()
        region.save()
    return region


def get_entry(uri):
    source_id = regex_entry.findall(uri)[0]
    return(get_entry_by_id(source_id))

def get_entry_by_id(source_id):
    try:
        entry = Entry.objects.get(source_id=source_id)
    except ObjectDoesNotExist:
        print("no entry")
        entry = Entry(source_id=source_id)
        vgo = VegGuideObject('http://www.vegguide.org/entry/%s' % source_id)
        entry.results_source = vgo.results_json
        entry.modified_source = datetime.datetime.now()
        obj = json.loads(entry.results_source)
        region_uri = obj['region']['uri']
        region = get_region(region_uri)
        entry.region = region
        entry.save()
    return entry

geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"

def get_entry_geo(entry):
    obj = json.loads(entry.results_source)
    address_prepared = entry.get_address_str().replace(' ', '+')
    if not entry.results_geo:
        url = geocode_url % (address_prepared, settings.GOOGLE_GEOCODE_API_KEY)
        req = request.urlopen(url)
        data = req.readall().decode('utf-8')
        result = data
        entry.results_geo = result
        entry.save()
    return entry.get_cord()


    

    


    






if __name__ == '__main__':
    print(get_entry('https://www.vegguide.org/entry/20647'))