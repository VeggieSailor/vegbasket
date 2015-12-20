from django.test import TestCase

from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id
from vegbasketapp.content.tools import get_entry_by_vg_id

from vegbasketapp.content.tools import convert_region
from vegbasketapp.content.models import VeggieSailorRegion
from django.core.urlresolvers import reverse


class ToolsTestCase(TestCase):
    """Main class for the tools tests.
    """
    def test_convert_region_by_id(self):
        """Test convert region by id.
        """
        region = get_region_by_id(52)
        vs_region = convert_region(52)
        region.set_obj()
        self.assertEqual(region.obj['name'], 'Europe')
        self.assertEqual(region.obj['name'], vs_region.name)    
    
    def test_entry_attributes(self):
        """Perform various test on the entry.
        """
        entry = get_entry_by_vg_id(20704)
        entry.get_images_600_400()
        self.assertIn('Barcelona', entry.region.__str__())
        self.assertIn('Villa', entry.__unicode__())
        self.assertIn('Villa', entry.__str__())
        
        

        
class SearchTest(TestCase):
    """Tests for the entries.
    
    """
    def test_basic_search(self):
        """Test static example entry view.
        
        """
        c = Client()
        r = c.get(reverse('search_view'))
        self.assertEqual(r.content.decode('utf-8').find('Veggie Sailor')>-1,True)

