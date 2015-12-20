from django.test import TestCase
from django.test import Client

from vegbasketapp.content.models import VeggieSailorRegion
from django.core import serializers
from vegbasketapp.content.models import *
from vegbasketapp.transformer.models import *


class HomeTestCase(TestCase):
    #fixtures = ["region_home.json", "entry_home.json","vs_region_home.json","vs_entry_home.json", "vs_image_home.json"]
    #fixtures = ['region_home.json', 'entry_home.json']
    fixtures = ["region_home.json", "entry_home.json","vs_region_home.json",
                "vs_entry_home.json", "vs_image_home.json",
                "vs_cuisine_home.json","vs_tag_home.json",
                "vs_category_home.json", "vs_payment_home.json"]
    # def test_create_user(self):
    #     from picupwebapp.picture.models  import Picture, Gallery
    #     from django.contrib.auth.models import User
    #     u = User(username="test")
    #     u.save()
    #     self.assertEqual(u.id>0,True)

    def test_home_page(self):
        c = Client()
        r = c.get('/')
        self.assertEqual(r.content.decode('utf-8').find('vegan')>-1,True)



        #data = serializers.serialize("json", Region.objects.all())
        #f = open('/tmp/region_home.json', 'w')
        #f.write(data)
        #f.close()       
        
        #data = serializers.serialize("json", Entry.objects.all())
        #f = open('/tmp/entry_home.json', 'w')
        #f.write(data)        
        #f.close()
        
        #data = serializers.serialize("json", VeggieSailorRegion.objects.all())
        #f = open('/tmp/vs_region_home.json', 'w')
        #f.write(data)
        #f.close()               
        #data = serializers.serialize("json", VeggieSailorEntry.objects.all())
        #f = open('/tmp/vs_entry_home.json', 'w')
        #f.write(data)        
        #f.close()               
        
        #data = serializers.serialize("json", VeggieSailorImage.objects.all())
        #f = open('/tmp/vs_image_home.json', 'w')
        #f.write(data)                
        #f.close()       
        
        #data = serializers.serialize("json", VeggieSailorCuisine.objects.all())
        #f = open('/tmp/vs_cuisine_home.json', 'w')
        #f.write(data)            
        #f.close()       
        
        #data = serializers.serialize("json", VeggieSailorCategory.objects.all())
        #f = open('/tmp/vs_category_home.json', 'w')
        #f.write(data)                
        #f.close()       
        
        #data = serializers.serialize("json", VeggieSailorPayment.objects.all())
        #f = open('/tmp/vs_payment_home.json', 'w')
        #f.write(data)                
        #f.close()               

        #data = serializers.serialize("json", VeggieSailorTag.objects.all())
        #f = open('/tmp/vs_tag_home.json', 'w')
        #f.write(data)                
        #f.close()               
        
        
        

