from random import randint
from time import sleep

from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.conf import settings
from django.test import TestCase, Client
from django.core import serializers

from vegbasketapp.transformer.tools_entry import get_region_by_id
from vegbasketapp.content.tools import get_entry_by_vg_id
from vegbasketapp.transformer.models import Entry
from vegbasketapp.content.tools import convert_region
from vegbasketapp.content.models import VeggieSailorRegion
from vegbasketapp.content.models import *

class Command(BaseCommand):
    args = ''
    help = 'Converts all entries'
    def handle(self, *args, **options):
        vg_entry_id = 12188
        vg_entry = get_entry_by_vg_id(vg_entry_id)
        
        
        data = serializers.serialize("json", Entry.objects.filter(source_id=vg_entry_id))
        file_json = open('/tmp/vg_entry_%s.json' % vg_entry_id, 'w')
        file_json.write(data)
        file_json.close()

