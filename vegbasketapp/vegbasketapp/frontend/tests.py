from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.core import serializers
from vegbasketapp.content.models import *
from vegbasketapp.transformer.models import *     
class EntryTest(TestCase):
    """Tests for the entries.
    
    """
    fixtures = ['region_frontend.json', 'entry_frontend.json', 
                'vs_entry_frontend.json', 'vs_image_frontend.json', 
                'vs_region_frontend.json','vs_payment_frontend.json',
                'vs_category_frontend.json','vs_cuisine_frontend.json',
                'vs_tag_frontend.json']
    def test_view_get_example_entry(self):
        """Test static example entry view.
        
        """
        c = Client()
        r = c.get(reverse('entry_example'))
        self.assertEqual(r.content.decode('utf-8').find('Hotel')>-1,True)
        
    def test_view_flax(self):
        """Test name of the place.
                
        """        
        c = Client()
        r = c.get(reverse('entry_vg',args=('20647',)), follow=True)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.content.decode('utf-8').find('Flax')>-1,True)        

    def test_view_other_enjoy(self):
        """Test category other in Enjoy.
                
        """        
        c = Client()
        r = c.get(reverse('entry_vg',args=('20703',)), follow=True)
        self.assertEqual(r.content.decode('utf-8').find('Other')>-1,True)     
        
        
    def test_view_african_ugarit(self):
        """Test food type in Ugarit.
                
        """        
        c = Client()
        r = c.get(reverse('entry_vg',args=('20704',)), follow=True)
        self.assertEqual(r.content.decode('utf-8').find('African')>-1,True)
        
        #r = c.get(reverse('entry_vg',args=('20703',)), follow=True)
        #r = c.get(reverse('entry_vg',args=('20647',)), follow=True)
        
   
        
        #data = serializers.serialize("json", Region.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/region_frontend.json', 'w')
        #f.write(data)
        #f.close()    

        #data = serializers.serialize("json", Entry.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/entry_frontend.json', 'w')
        #f.write(data)
        #f.close()
        
        #data = serializers.serialize("json", VeggieSailorImage.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/vs_image_frontend.json', 'w')
        #f.write(data)
        #f.close()   
        
        #data = serializers.serialize("json", VeggieSailorEntry.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/vs_entry_frontend.json', 'w')
        #f.write(data)
        #f.close()      
        
        #data = serializers.serialize("json", VeggieSailorRegion.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/vs_region_frontend.json', 'w')
        #f.write(data)
        #f.close()            
        #data = serializers.serialize("json", VeggieSailorCuisine.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/vs_cuisine_frontend.json', 'w')
        #f.write(data)            
        #f.close()       
    
        #data = serializers.serialize("json", VeggieSailorCategory.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/vs_category_frontend.json', 'w')
        #f.write(data)                
        #f.close()       
    
        #data = serializers.serialize("json", VeggieSailorPayment.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/vs_payment_frontend.json', 'w')
        #f.write(data)                
        #f.close()               
    
        #data = serializers.serialize("json", VeggieSailorTag.objects.all())
        #f = open('vegbasketapp/frontend/fixtures/vs_tag_frontend.json', 'w')
        #f.write(data)                
        #f.close()               
        
        #from ipdb import set_trace; set_trace()