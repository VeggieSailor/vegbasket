from django.core.management.base import BaseCommand, CommandError
from vegbasketapp.content.models import VeggieSailorEntry, VeggieSailorRegion
from django.utils import translation
from django.core.urlresolvers import reverse
import yandex_translate
from django.conf import settings

class Command(BaseCommand):
    """Translate all the regions"""

    def handle(self, *args, **options):
        names = [ x.name for x in VeggieSailorRegion.objects.all() ]
        DEST_FILE = '/tmp/translations_ru.csv'
        fd = open(DEST_FILE, 'w')
        translator = yandex_translate.YandexTranslate(settings.YANDEX_TRANSLATE_KEY)
        for name in names:
            
            result = translator.translate(name, 'en-ru')
            #{'code': 200, 'lang': 'en-ru', 'text': ['Северная Америка']}
            if result['code']==200:
                line = '%s||%s\n' % (name, result['text'][0])
            else:
                line = '%s||||\n' % (name, )
            print (line)
            fd.write(line)
            fd.flush()
        fd.close()
            
            
        
