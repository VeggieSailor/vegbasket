from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.models import VeggieSailorEntry, VeggieSailorRegion
from django.utils import translation
from django.core.urlresolvers import reverse

class Command(BaseCommand):
    """Generate Sitemap"""

    def handle(self, *args, **options):
        """Main method.
        """

        LANGS = ('ru', 'en')
        entries = VeggieSailorEntry.objects.all()
        regions = VeggieSailorRegion.objects.all()
        for lang in LANGS:
            translation.activate(lang)
            for entry in entries:
                print ('https://veggiesailor.com%s' % (entry.get_absolute_url()))
            for region in regions:
                print ('https://veggiesailor.com%s?q=%s' % (reverse("search_view"),region.name))
