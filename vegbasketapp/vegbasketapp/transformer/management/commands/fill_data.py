from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.transformer.tools_entry import get_entry,get_entry_geo
from django.conf import settings

class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    # help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        entry = get_entry('https://www.vegguide.org/entry/20647')
        print(get_entry_geo(entry))
        # print(entry.get_address_str())
        # print(settings.GOOGLE_GEOCODE_API_KEY)
        # for poll_id in args:
        #     try:
        #         poll = Poll.objects.get(pk=int(poll_id))
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write('Successfully closed poll "%s"' % poll_id)