from django.test import TestCase

from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id

from vegbasketapp.content.tools import convert_region

from vegbasketapp.content.models import VeggieSailorRegion


class ToolsTestCase(TestCase):
    def test_convert_region_by_id(self):
        get_region_by_id(66)
        region, vs_region = convert_region(66)
        region.set_obj()
        self.assertEqual(region.obj['name'], 'Spain')
        self.assertEqual(region.obj['name'], vs_region.name)


