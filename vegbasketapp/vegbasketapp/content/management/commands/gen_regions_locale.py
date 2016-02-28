from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.models import VeggieSailorEntry, VeggieSailorRegion
from django.utils import translation
from django.core.urlresolvers import reverse

from django.conf import settings

class Command(BaseCommand):
    """Prepare to translate all the regions"""

    def handle(self, *args, **options):
        names = [ x.name for x in VeggieSailorRegion.objects.all() ]
        for name in names:
            print ("{%% trans '%s' %%}" % name)
