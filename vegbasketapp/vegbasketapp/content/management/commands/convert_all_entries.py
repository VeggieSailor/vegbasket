from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.tools import convert_entry

from vegbasketapp.transformer.models import Entry

class Command(BaseCommand):
    args = ''

    help = 'Converts all entries'

    def handle(self, *args, **options):
        entries = Entry.objects.all()
        
            
        for entry in entries:
            print (entry.source_id)
            convert_entry(entry.source_id)



        