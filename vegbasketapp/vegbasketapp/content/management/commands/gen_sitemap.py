from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.models import VeggieSailorEntry, VeggieSailorRegion




class Command(BaseCommand):
    """Generate Sitemap"""

    def handle(self, *args, **options):
        """Main method.
        """
        

        entries = VeggieSailorEntry.objects.all()
        for entry in entries:
            print ('https://veggiesailor.com%s' % entry.get_absolute_url())
            
        regions = VeggieSailorRegion.objects.all()        
        for region in regions:
            print ('https://veggiesailor.com/search/?q=%s' % region.name)


        