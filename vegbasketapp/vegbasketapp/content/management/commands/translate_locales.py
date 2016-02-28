from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.models import VeggieSailorEntry, VeggieSailorRegion
from django.utils import translation
from django.core.urlresolvers import reverse

from django.conf import settings
import polib

import csv

class Command(BaseCommand):
    """Prepare to translate all the regions"""
    def add_arguments(self, parser):
        parser.add_argument('src',  type=str)
        parser.add_argument('dst',  type=str)

    def handle(self, *args, **options):
        print (options['src'])
        print (options['dst'])
        po = polib.pofile(options['dst'])
        with open(options['src']) as csvfile:
            transreader = csv.reader(csvfile, delimiter=';')
            for row in transreader:
                po_row = po.find(row[0])
                if po_row:
                    print (row[0])
                    po_row.msgstr = row[1]
                    
                    
        po.save()
