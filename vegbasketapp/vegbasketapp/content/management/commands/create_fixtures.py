from random import randint
from time import sleep

from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.tools import convert_entry

from vegbasketapp.transformer.models import Entry

from django.conf import settings
from django.test import TestCase, Client

from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id
from vegbasketapp.content.tools import get_entry_by_vg_id

from vegbasketapp.content.tools import convert_region
from vegbasketapp.content.models import VeggieSailorRegion
from django.core.urlresolvers import reverse

from vegbasketapp.content.models import VeggieSailorRegion
from django.core import serializers
from vegbasketapp.content.models import *

class Command(BaseCommand):
    args = ''

    help = 'Converts all entries'

    def handle(self, *args, **options):
        regions_ids = (2218,844,2218,336,52, 583, 328,298,52, 301, 300,74,72,70, 106, 16,1,2, 3, 356, 355, 274, 273, )
        
        for region_id in regions_ids:
            get_region_by_id(region_id)
            convert_region(region_id)

        data = serializers.serialize("json", Region.objects.filter(source_id__in=regions_ids))
        f = open('/tmp/region_52.json', 'w')
        f.write(data)
        f.close()
        data = serializers.serialize("json", VeggieSailorRegion.objects.filter(source_region__source_id__in=regions_ids))
        f = open('/tmp/vs_region_source_52.json', 'w')
        f.write(data)
        f.close()       

        

