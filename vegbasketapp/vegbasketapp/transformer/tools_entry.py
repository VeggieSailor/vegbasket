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
    try:
        entry = Entry.objects.get(source_id=source_id)
    except ObjectDoesNotExist:
        print("no entry")
        entry = Entry(source_id=source_id)
        vgo = VegGuideObject(uri)
        entry.results_source = vgo.results_json
        entry.modified_source = datetime.datetime.now()

        obj = json.loads(entry.results_source)
        print("AAAAAAAAA", type(vgo.results_json))
        region_uri = obj['region']['uri']
        print(region_uri)
        region = get_region(region_uri)
        entry.region = region
        entry.save()
    return entry

geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"

def get_entry_geo(entry):
    obj = json.loads(entry.results_source)
    address_prepared = entry.get_address_str().replace(' ', '+')
    print("URL",address_prepared)
    if not entry.results_geo:
        print('fetching_data')
        url = geocode_url % (address_prepared, settings.GOOGLE_GEOCODE_API_KEY)
        print(url)
        req = request.urlopen(url)
        data = req.readall().decode('utf-8')
        result = data
        entry.results_geo = result
        entry.save()


    data = json.loads(entry.results_geo)
    print(data.keys(), data['results'][0]['geometry']['location'].keys())

    lng = data['results'][0]['geometry']['location']['lng']
    lat = data['results'][0]['geometry']['location']['lat']

    return {'lng': lng, 'lat':lat}


    

    


    






if __name__ == '__main__':
    print(get_entry('https://www.vegguide.org/entry/20647'))