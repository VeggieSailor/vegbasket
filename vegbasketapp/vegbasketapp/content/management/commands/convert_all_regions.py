from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.tools import convert_region

from vegbasketapp.transformer.models import Region

class Command(BaseCommand):
    args = ''

    help = 'Converts all regions'

    def handle(self, *args, **options):
        regions = Region.objects.all()
        regions_source_ids = (elem.source_id for elem in regions)
        for region_source_id in regions_source_ids:
            convert_region(region_source_id)



        