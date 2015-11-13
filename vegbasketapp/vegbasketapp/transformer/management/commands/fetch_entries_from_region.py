from django.core.management.base import BaseCommand, CommandError
#from vegbasketapp.transformer.tools_entry import get_entry,get_entry_geo
from django.conf import settings
from vegbasketapp.transformer.tools_entry import get_entry_by_id,get_entry_geo, get_region_by_id, get_entries, get_entry

from json import loads

from time import sleep
from random import randint

class Command(BaseCommand):
    args = '<region_id region_id ...>'

    def handle(self, *args, **options):
        print(args)
        for region_id in args:
            try:
                print("getting region", region_id)
                region = get_region_by_id(region_id)
                region.set_obj()
                entries = get_entries(region.obj['uri'])
                for result in entries.results:
                    print(result['uri'])
                    get_entry(result['uri'])
                    sleep(1)
                sleep_time = randint(2, 5)
                print("sleeping", sleep_time)
                sleep(sleep_time)
            except KeyError:
                print("key error")
                

        self.stdout.write('Successfully got data')