from random import randint
from time import sleep

from django.core.management.base import BaseCommand
from vegbasketapp.content.tools import convert_entry

from vegbasketapp.transformer.models import Entry

from django.conf import settings

def sleep_random(min, max):
    """Sleep random time.    
    """
    sleep_time = randint(min, max)
    sleep(sleep_time)
    
class Command(BaseCommand):
    args = ''
    help = 'Converts all entries'

    def handle(self, *args, **options):
        entries = Entry.objects.all().order_by('source_id')
        for entry in entries:
            try:
                convert_entry(entry.source_id)
                if entry.get_elem("images"):
                    #print ("Had images, wait...")
                    if settings.DEBUG==False and False:
                        sleep_random(2,5)
            except KeyError:
                print ("ERROR with", entry.source_id)



        