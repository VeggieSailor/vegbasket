from django.test import TestCase
from django.test import Client

class EntryTest(TestCase):
    """Tests for the entries.
    
    """
    def test_view_get_example_entry(self):
        """Test static example entry view.
        
        """
        c = Client()
        r = c.get('/frontend/entry_example/')
        self.assertEqual(r.content.decode('utf-8').find('Hotel')>-1,True)
        
    def test_view_flax(self):
        """Test name of the place.
                
        """        
        c = Client()
        r = c.get('/frontend/e/vg/20647')
        self.assertEqual(r.content.decode('utf-8').find('Flax')>-1,True)        

    def test_view_other_enjoy(self):
        """Test category other in Enjoy.
                
        """        
        c = Client()
        r = c.get('/frontend/e/vg/20703')
        self.assertEqual(r.content.decode('utf-8').find('Other')>-1,True)     
        
        
    def test_view_african_ugarit(self):
        """Test food type in Ugarit.
                
        """        
        c = Client()
        r = c.get('/frontend/e/vg/20704')
        self.assertEqual(r.content.decode('utf-8').find('African')>-1,True)            

    

    