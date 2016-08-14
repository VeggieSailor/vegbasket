import datetime
from random import randint
from time import sleep

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import parsedatetime as pdt

from vegbasketapp.content.tools import convert_entry
from vegbasketapp.transformer.models import Entry
from vegbasketapp.content.models import VeggieSailorOpeningHour, \
     VeggieSailorEntry

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
cal = pdt.Calendar()

class Command(BaseCommand):
    """Convert all hours class.
    """
    args = ''

    help = 'Converts all entries'

    def handle(self, *args, **options):
        """Main 'handle' function.
        """
        objects_ids = list(set([ x['entry_id'] for x in VeggieSailorOpeningHour.objects.all().values("entry_id") ]))
        all_entries = Entry.objects.exclude(id__in=objects_ids)
        for entry in all_entries:
            try:
                vse = VeggieSailorEntry.objects.get(vg_object_id = entry.source_id)
                VeggieSailorOpeningHour.objects.filter(entry = vse).delete()
                hours = entry.get_elem('hours')
                for elem in hours:
                    days = (elem['days'])
                    if days in DAYS:
                        result = [DAYS.index(days)]

                    elif days.find('-')>-1:
                        result = [ DAYS.index(x) for x in  (days.split(' - ')) ]
                        result = list(range(result[0], result[1]+1))
                    for new_elem in result:
                        try:
                            #print (DAYS[new_elem], new_elem)
                            #print (hours)
                            for hour in elem['hours']:
                                parsed_hours = hour.split(' - ')
                                #print (parsed_hours)
                                if parsed_hours[0] == 'closed':
                                    #print ("closed!")
                                    is_closed = True
                                else:
                                    #print (hour[0], hour[1])
                                    td = cal.parseDT(parsed_hours[1])[0] - cal.parseDT(parsed_hours[0])[0]
                                    #print (td, type(td))
                                    opening_time = cal.parseDT(parsed_hours[0])[0]
                                    is_closed = False
                                    #print (parsed_hours[0],td, opening_time.hour, opening_time.minute)
                            vsoh = VeggieSailorOpeningHour()
                            vsoh.entry = vse
                            vsoh.weekday = new_elem
                            vsoh.from_hour = datetime.time(hour=opening_time.hour,minute=opening_time.minute)
                            vsoh.duration = td
                            vsoh.is_closed = is_closed
                            vsoh.save()
                        except IndexError:
                            print("Index Error: %s" % (entry.id))
            except VeggieSailorEntry.DoesNotExist:
                print("Not Exists: %s" % (entry.id))
