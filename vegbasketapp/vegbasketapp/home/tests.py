from django.test import TestCase
from django.test import Client
from vegbasketapp.transformer.tools_entry import get_entry_by_id,get_entry_geo



class EntryTestCase(TestCase):
    def test_get_entry(self):
        c = Client()
        r = c.get('/transformer/entry/12188')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_get_region(self):
        c = Client()
        r = c.get('/transformer/region/66')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_get_map(self):
        c = Client()
        r = c.get('/transformer/entry/12188/map')
        self.assertEqual(r.content.decode('utf-8').find('2.1773')>-1,True)

	def test_get_reviews(self):
        c = Client()
        r = c.get('/transformer/entry/12188/reviews')
        self.assertEqual(r.content.decode('utf-8').find('traditional')>-1,True)





