from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.models import VeggieSailorEntry, VeggieSailorRegion
from django.utils import translation
from django.core.urlresolvers import reverse
import yandex_translate
from django.conf import settings

class Command(BaseCommand):
    """Translate all the regions"""

    def handle(self, *args, **options):
        print (args)
        