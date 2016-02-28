from random import randint

from django.core.management.base import BaseCommand
from vegbasketapp.content.tools import convert_entry

from vegbasketapp.transformer.models import Entry

from django.conf import settings

class Command(BaseCommand):
    args = ''

    help = 'Converts an entry'


    def add_arguments(self, parser):
        parser.add_argument('entry_id', nargs='+', type=int)

    def handle(self, *args, **options):
        print (args, options['entry_id'])
        for entries_id in options['entry_id']:
            entry = Entry.objects.get(source_id=entries_id)
            convert_entry(entry.source_id, True)
