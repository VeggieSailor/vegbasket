from unittest import mock

from django.test import TestCase
from django.test import Client
from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id
from vegbasketapp.transformer.tools_entry import get_entry_geo


from django.core import serializers
from vegbasketapp.content.models import *
from vegbasketapp.transformer.models import *

from vegbasketapp.transformer.vegguide import VegGuideParser

REGION_23 = """
{
   "parent" : {
      "is_country" : "1",
      "entries_uri" : "http://www.vegguide.org/region/19/entries",
      "name" : "Canada",
      "uri" : "http://www.vegguide.org/region/19",
      "entry_count" : "0"
   },
   "entries_uri" : "http://www.vegguide.org/region/23/entries",
   "name" : "Ontario",
   "children" : [
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/2338/entries",
         "name" : "Barrie",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/2338",
         "entry_count" : "3"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/409/entries",
         "name" : "Bruce Peninsula",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/409",
         "entry_count" : "0"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/813/entries",
         "name" : "Burlington",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/813",
         "entry_count" : "4"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1913/entries",
         "name" : "Chatham-Kent",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1913",
         "entry_count" : "2"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1851/entries",
         "name" : "Collingwood",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1851",
         "entry_count" : "2"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1943/entries",
         "name" : "Dorset",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1943",
         "entry_count" : "1"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/718/entries",
         "name" : "Durham",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/718",
         "entry_count" : "1"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/450/entries",
         "name" : "Guelph",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/450",
         "entry_count" : "8"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/289/entries",
         "name" : "Hamilton",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/289",
         "entry_count" : "34"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/368/entries",
         "name" : "Kingston",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/368",
         "entry_count" : "3"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/459/entries",
         "name" : "Kitchener-Waterloo",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/459",
         "entry_count" : "14"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1975/entries",
         "name" : "Lion's Head",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1975",
         "entry_count" : "3"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/408/entries",
         "name" : "London",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/408",
         "entry_count" : "10"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/687/entries",
         "name" : "Markham",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/687",
         "entry_count" : "4"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/2553/entries",
         "name" : "Mississauga",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/2553",
         "entry_count" : "14"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/522/entries",
         "name" : "Muskoka",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/522",
         "entry_count" : "2"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/2351/entries",
         "name" : "Newmarket",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/2351",
         "entry_count" : "2"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/760/entries",
         "name" : "Niagara Falls",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/760",
         "entry_count" : "12"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1238/entries",
         "name" : "North Bay",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1238",
         "entry_count" : "5"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/849/entries",
         "name" : "Oakville",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/849",
         "entry_count" : "2"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/2216/entries",
         "name" : "Oshawa",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/2216",
         "entry_count" : "1"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/135/entries",
         "name" : "Ottawa",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/135",
         "entry_count" : "40"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/689/entries",
         "name" : "Peterborough",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/689",
         "entry_count" : "3"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1837/entries",
         "name" : "Sarnia",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1837",
         "entry_count" : "0"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1260/entries",
         "name" : "Sault Ste. Marie",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1260",
         "entry_count" : "1"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/1924/entries",
         "name" : "Stratford",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/1924",
         "entry_count" : "2"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/2595/entries",
         "name" : "Sudbury",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/2595",
         "entry_count" : "1"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/891/entries",
         "name" : "Thunder Bay",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/891",
         "entry_count" : "7"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/124/entries",
         "name" : "Toronto",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/124",
         "entry_count" : "161"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/2180/entries",
         "name" : "Uxbridge",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/2180",
         "entry_count" : "2"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/2406/entries",
         "name" : "Welland",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/2406",
         "entry_count" : "0"
      },
      {
         "is_country" : "0",
         "entries_uri" : "http://www.vegguide.org/region/407/entries",
         "name" : "Windsor",
         "time_zone" : "America/Montreal",
         "uri" : "http://www.vegguide.org/region/407",
         "entry_count" : "5"
      }
   ],
   "uri" : "http://www.vegguide.org/region/23",
   "entry_count" : "0",
   "is_country" : "0",
   "time_zone" : "America/Montreal"
}

"""

class MockTestCase(TestCase):
    """Some tests with mocks.
    """
    @mock.patch('vegbasketapp.transformer.vegguide.VegGuideParser', autospec=True)
    def test_request(self, VegGuideParser):
        VegGuideParser.return_value.result = json.loads(REGION_23)
        vg_region =  (get_region_by_id(23))
        vg_region.set_obj()
        self.assertEqual(vg_region.obj['name'], 'Ontario')

class MockTestCaseFixtures(TestCase):
    """Some tests with mocks.
    """
    fixtures = ['entry_transformer.json','region_transformer.json','reviews_transformer.json']
    @mock.patch('vegbasketapp.transformer.vegguide.VegGuideParser', autospec=True)
    def test_geo(self, VegGuideParser):
        vg_entry = get_entry_by_id(12188)
        cords = get_entry_geo(vg_entry)
        #VegGuideParser.return_value.result = json.loads(REGION_23)
        #vg_region =  (get_region_by_id(23))
        #vg_region.set_obj()
        #self.assertEqual(vg_region.obj['name'], 'Ontario')


class ViewsTestCase(TestCase):
    fixtures = ['entry_transformer.json','region_transformer.json','reviews_transformer.json']
    def test_view_get_entry(self):
        c = Client()
        r = c.get('/transformer/entry/12188')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_view_get_entry_force(self):
        c = Client()
        r = c.get('/transformer/entry/12188?force=False')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_view_get_region(self):
        c = Client()
        r = c.get('/transformer/region/66')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_view_get_region_force(self):
        c = Client()
        r = c.get('/transformer/region/66?force=False')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    #def test_view_get_map(self):
    #    c = Client()
    #    r = c.get('/transformer/entry/12188/map')
    #    self.assertEqual(r.content.decode('utf-8').find('2.1773')>-1,True)

    def test_view_get_reviews(self):
        c = Client()
        r = c.get('/transformer/entry/12188/reviews')
        self.assertEqual(r.content.decode('utf-8').find('traditional')>-1,True)

class ToolsTestCase(TestCase):
    fixtures = ['entry_transformer.json','region_transformer.json','reviews_transformer.json']
    def test_get_entry_by_id(self):
        entry = get_entry_by_id(12188)
        entry.set_obj()
        self.assertEqual(entry.obj['name'], 'Gopal')

    def test_get_entry_by_id_force(self):
        entry = get_entry_by_id(12188)
        entry = get_entry_by_id(12188, force=False)
        entry.set_obj()
        self.assertEqual(entry.obj['name'], 'Gopal')

    def test_get_region_by_id(self):
        region = get_region_by_id(66)
        region.set_obj()
        self.assertEqual(region.obj['name'], 'Spain')

    def test_get_region_by_id_force(self):
        region = get_region_by_id(66, force=False)
        region.set_obj()
        self.assertEqual(region.obj['name'], 'Spain')


        #entry = get_entry_by_id(12188)
        #entry.set_obj()
        #self.assertEqual(entry.obj['name'], 'Gopal')

        #entry = get_entry_by_id(12188)
        #entry = get_entry_by_id(12188, force=True)
        #entry.set_obj()
        #self.assertEqual(entry.obj['name'], 'Gopal')

    
        #region = get_region_by_id(66)
        #region.set_obj()
        #self.assertEqual(region.obj['name'], 'Spain')
        #c = Client()
        #r = c.get('/transformer/entry/12188/reviews')
    
        #region = get_region_by_id(66, force=False)
        #region.set_obj()
        #self.assertEqual(region.obj['name'], 'Spain')

        #c = Client()
        #r = c.get('/transformer/entry/12188')
        #self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

        #c = Client()
        ##r = c.get('/transformer/entry/12188?force=True')
        #self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)


        #c = Client()
        #r = c.get('/transformer/region/66')

        #data = serializers.serialize("json", Region.objects.all())
        #f = open('vegbasketapp/transformer/fixtures/region_transformer.json', 'w')
        #f.write(data)
        #f.close()       
    
        #data = serializers.serialize("json", Entry.objects.all())
        #f = open('vegbasketapp/transformer/fixtures/entry_transformer.json', 'w')
        #f.write(data)        
        #f.close()
        
        #data = serializers.serialize("json", Reviews.objects.all())
        #f = open('vegbasketapp/transformer/fixtures/reviews_transformer.json', 'w')
        #f.write(data)        
        #f.close()        