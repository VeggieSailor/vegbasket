from django.core.management.base import BaseCommand
from vegbasketapp.content.tools import convert_region_down

class Command(BaseCommand):
    """Convert all regions.
    """
    args = '<regions>'
    help = 'Converts all regions'

    def handle(self, *args, **options):
        """Main method.
        """
        if args:
            elems = args
        else:
            elems = [52, 1, 35, 24, 28, 614, 81, 637, 83, 70, 1677]
            
        for region_source_id in elems:
            convert_region_down(region_source_id)
