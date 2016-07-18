from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.models import VeggieSailorEntry, VeggieSailorRegion
from django.utils import translation
from django.core.urlresolvers import reverse
from vegbasketapp.transformer.tools_entry import get_entry_by_id, \
     get_reviews_by_entry_id, get_region_by_id, get_entry_geo  
from django.conf import settings
from vegbasketapp.transformer.models import Entry 

class Command(BaseCommand):
    """Fill all the cords"""

    def handle(self, *args, **options):
        vses = VeggieSailorEntry.objects.all()
        counter = 0
        for vsee in vses:
            source_id = vsee.object_id
            e = Entry.objects.get(id=source_id)
            try:
                cords = get_entry_geo(e) 
                vsee.long = cords['lng']
                vsee.lat = cords['lat']
                vsee.save()
                print (cords)
            except:
                counter += 1
        print (counter)
            

