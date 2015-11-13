from django.core.management.base import BaseCommand, CommandError
#from vegbasketapp.transformer.tools_entry import get_entry,get_entry_geo
from django.conf import settings
from vegbasketapp.transformer.tools_entry import get_entry_by_id,get_entry_geo

class Command(BaseCommand):
    """Fill data for entries.
    """
    args = '<entry_id entry-id ...>'

    def handle(self, *args, **options):
        print(args)
        for entry_id in args:
            print("getting", entry_id)
            entry = get_entry_by_id(entry_id)
            print("got, back to cords", entry_id)
            print(get_entry_geo(entry))
            print(entry.get_cord())
            print(get_entry_geo(entry))
            print(entry.get_address_str())
            print(settings.GOOGLE_GEOCODE_API_KEY)
        self.stdout.write('Successfully got data')