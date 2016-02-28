from django.test import TestCase, Client

from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id
from vegbasketapp.content.tools import get_entry_by_vg_id, convert_region_down

from vegbasketapp.content.tools import convert_region
from vegbasketapp.content.models import VeggieSailorRegion
from django.core.urlresolvers import reverse

from django.core import serializers
from vegbasketapp.content.models import *
from vegbasketapp.transformer.models import *
from vegbasketapp.content.tools import get_region_id
from django.core.management import call_command
from django.utils.six import StringIO


class CommandTestCase(TestCase):
    """Class for testing the commands. Coverage.
    """
    fixtures = ["region_52.json","entry_52.json", "vs_region_source_52.json",]    
    def test_command_convert_all_entries(self):
        """Convert all entries test.
        """
        out = StringIO()
        call_command('convert_all_entries', stdout=out)
        self.assertEqual('', out.getvalue())

    def test_command_convert_all_regions(self):
        """Convert all regions test.
        """
        out = StringIO()
        call_command('convert_all_regions', '23', stdout=out)
        self.assertEqual('', out.getvalue())
        
    def test_command_convert_hours(self):
        """Convert hours test.
        """
        out = StringIO()
        call_command('convert_hours', stdout=out)
        self.assertEqual('', out.getvalue())


class SimplyTestCase(TestCase):
    """Simply tests to fix the coverage.
    """
    
    def test_get_region_id(self):
        """Test getting region number.
        """
        url = 'https://www.vegguide.org/region/35'
        region_id = get_region_id(url)
        self.assertAlmostEqual(region_id, '35')

    def test_convert_region_23(self):
        """Test if name fits - coverage.
        """
        vs_region = convert_region(23)
        self.assertEqual(vs_region.name, 'Ontario')

class ToolsTestCase(TestCase):
    """Main class for the tools tests.
    """
    fixtures = ["region_52.json","entry_52.json", "vs_region_source_52.json",]
    def test_convert_region_by_id(self):
        """Test convert region by id.
        """

        region = get_region_by_id(52)
        
        regions_ids = (52, 583,66)
        
        for region_id in regions_ids:
            get_region_by_id(region_id)
            convert_region(region_id)
        
        
        vs_region = convert_region(52)
        region.set_obj()
        self.assertEqual(region.obj['name'], 'Europe')
        self.assertEqual(region.obj['name'], vs_region.name)
        
        #regions_ids = (22, 2218,844,2218,336,52, 583, 328,298,52, 301, 300,74,72,70, 106, 16,1,2, 3, 356, 355, 274, 273, )
        
        #for region_id in regions_ids:
            #get_region_by_id(region_id)
            #convert_region(region_id)

        #return True
        #data = serializers.serialize("json", Region.objects.all())
        #f = open('vegbasketapp/content/fixtures/region_52.json', 'w')
        #f.write(data)
        #f.close()
   
        #data = serializers.serialize("json", VeggieSailorRegion.objects.all())
        #f = open('vegbasketapp/content/fixtures/vs_region_source_52.json', 'w')
        #f.write(data)
        #f.close()     
        

        
    def test_convert_region_down(self):
        """Test convert_region_down.
        """
        region, vs_region = convert_region_down(23)
        self.assertEqual(vs_region.name, 'Ontario')
        self.assertEqual(region.source_id, 23)
    
    def test_entry_attributes(self):
        """Perform various test on the entry.
        """
      
        entry = get_entry_by_vg_id(20704)
        entry.get_images_600_400()
        self.assertIn('Barcelona', entry.region.__str__())
        self.assertIn('Villa', entry.__unicode__())
        self.assertIn('Villa', entry.__str__())
        
        #data = serializers.serialize("json", Entry.objects.all())
        #f = open('vegbasketapp/content/fixtures/entry_52.json', 'w')
        #f.write(data)
        #f.close()          

class SearchTest(TestCase):
    """Tests for the entries.
    
    """
    def test_basic_search(self):
        """Test static example entry view.
        
        """
        c = Client()
        r = c.get(reverse('search_view'))
        self.assertEqual(r.content.decode('utf-8').find('Veggie Sailor')>-1,True)

