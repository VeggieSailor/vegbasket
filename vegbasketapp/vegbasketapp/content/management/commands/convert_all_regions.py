from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.tools import convert_region_down

from vegbasketapp.transformer.models import Region

class Command(BaseCommand):
    args = '<regions>'

    help = 'Converts all regions'

    def handle(self, *args, **options):
        if args:
            elems = args
        else:
            elems = [52, 1, 35, 24, 28, 614, 81, 637, 83, 70, 1677]
            
        for region_source_id in elems:
            convert_region_down(region_source_id)



        