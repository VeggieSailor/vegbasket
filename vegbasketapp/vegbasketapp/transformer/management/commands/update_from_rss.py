from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.models import Entry
from vegbasketapp.content.tools import convert_entry
import xml.etree.ElementTree as etree
import urllib.request
import warnings
warnings.filterwarnings(
    'error', r"DateTimeField .* received a naive datetime",
    RuntimeWarning, r'django\.db\.models\.fields')
class Command(BaseCommand):
    """Update from rss.
    """
    help = 'Refresh new entries from the rss'

    def handle(self, *args, **options):
        url = 'http://www.vegguide.org/site/recent.rss?entries_only=1'
        req = urllib.request.urlopen(url)
        atom_data_entries = req.read().decode('utf-8')
        e = etree.fromstring(atom_data_entries)
        links = e.findall('channel/item/link')
        for link in links:
            source_id = int(link.text.split('entry/')[1])
            
            number = Entry.objects.filter(source_id=source_id).count()
            if number==0:
                print ("New entry %s" % source_id, number)
                convert_entry(source_id)
            get_entry_by_id(source_id, force=True)