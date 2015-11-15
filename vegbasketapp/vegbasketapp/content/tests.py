from django.test import TestCase

from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id

from vegbasketapp.content.tools import convert_region
from vegbasketapp.content.models import VeggieSailorRegion


#class ToolsTestCase(TestCase):
    #def test_convert_region_by_id(self):
        #region = get_region_by_id(52)
        #vs_region = convert_region(52)
        #region.set_obj()
        #self.assertEqual(region.obj['name'], 'Europe')
        #self.assertEqual(region.obj['name'], vs_region.name)



