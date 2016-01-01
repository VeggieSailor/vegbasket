from random import randint
from time import sleep

from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.tools import convert_entry

from vegbasketapp.transformer.models import Entry
import parsedatetime as pdt
from django.conf import settings

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
cal = pdt.Calendar()
    
class Command(BaseCommand):
    args = ''

    help = 'Converts all entries'

    def handle(self, *args, **options):
        e = Entry.objects.get(id=4015)
        hours = e.get_elem('hours')
        for elem in hours:
            days = (elem['days'])
            if days in DAYS:
                result = [DAYS.index(days)]
                
            elif days.find('-')>-1:
                result = [ DAYS.index(x) for x in  (days.split(' - ')) ]
                result = list(range(result[0], result[1]+1))
            for new_elem in result:
                print (DAYS[new_elem])
                #print (hours)
                for hour in elem['hours']:
                    parsed_hours = hour.split(' - ')
                    #print (parsed_hours)

                    if parsed_hours[0] == 'closed':
                        print ("closed!")
                    else:
                        #print (hour[0], hour[1])
                        td = cal.parseDT(parsed_hours[1])[0] - cal.parseDT(parsed_hours[0])[0]
                        #print (td, type(td))
                        print (parsed_hours[0],td)
            
                
            

        