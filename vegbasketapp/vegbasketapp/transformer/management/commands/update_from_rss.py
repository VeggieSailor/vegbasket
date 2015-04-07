from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from vegbasketapp.transformer.tools_entry import get_entry_by_id
import xml.etree.ElementTree as etree
import urllib.request

class Command(BaseCommand):
    help = 'Refresh new entries from the rss'

    def handle(self, *args, **options):
        url = 'http://www.vegguide.org/site/recent.rss?entries_only=1'
        req = urllib.request.urlopen(url)
        atom_data_entries = req.read().decode('utf-8')
        e = etree.fromstring(atom_data_entries)
        links = e.findall('channel/item/link')
        for link in links:
            source_id = int(link.text.split('entry/')[1])
            get_entry_by_id(source_id, force=True)