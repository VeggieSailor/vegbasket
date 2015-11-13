from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from vegbasketapp.transformer.tools_entry import get_region_by_id
from vegbasketapp.transformer.tools_entry import regex_region 
from vegbasketapp.transformer.tools_entry import is_cached_region
from vegbasketapp.transformer.models import Region
# import urllib.request
from time import sleep
from random import randint


def fetch_region_recursion(region_id, number):
    """Fetch regions in recursive way.

    Parameters
    ----------
    region_id : int start region
    number : int number of recursive calls
    """
    number = int(number)
    if number<1:
        return (region_id, 0)
    region = get_region_by_id(region_id)
    region.set_obj()
    if region_id==0:
        regions = region.obj['regions']['primary']
    else:
        regions = region.obj.get('children', [])

    for region in regions:
        source_id = regex_region.findall(region['uri'])[0]
        is_cached = is_cached_region(source_id)
        if not is_cached:
            number -= int(1)
            sleep(randint(3,7)) # Be nice for VegGuide.org
        (region_id, number) = fetch_region_recursion(source_id, int(number))
        if number==0:   
            return (region_id, 0)
    return (region_id, number)

class Command(BaseCommand):
    """Feth regions.
    """
    args = 'regions_number region_start'
    help = 'Fetches 20 regions'
    
    def handle(self, *args, **options):
        number = int(args[0])
        start = int(args[1])
        if number>100:
            number == 100
        (last_region, result) = fetch_region_recursion(start, number)    
        print("Finished on ", last_region)



        