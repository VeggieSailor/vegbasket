from django.test import TestCase
from django.test import Client

class ExampleEntry(TestCase):
    def test_view_get_example_entry(self):
        c = Client()
        r = c.get('/frontend/entry_example/')
        self.assertEqual(r.content.decode('utf-8').find('Hotel')>-1,True)
        
    def test_view_flax(self):
        c = Client()
        r = c.get('/frontend/e/vg/20647')
        self.assertEqual(r.content.decode('utf-8').find('Flax')>-1,True)        
        
    
    