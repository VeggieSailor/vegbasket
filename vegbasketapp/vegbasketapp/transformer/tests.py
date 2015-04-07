from django.test import TestCase
from django.test import Client
from vegbasketapp.transformer.tools_entry import get_entry_by_id
from vegbasketapp.transformer.tools_entry import get_region_by_id

class ViewsTestCase(TestCase):
    def test_view_get_entry(self):
        c = Client()
        r = c.get('/transformer/entry/12188')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_view_get_entry_force(self):
        c = Client()
        r = c.get('/transformer/entry/12188?force=True')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_view_get_region(self):
        c = Client()
        r = c.get('/transformer/region/66')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_view_get_region_force(self):
        c = Client()
        r = c.get('/transformer/region/66?force=True')
        self.assertEqual(r.content.decode('utf-8').find('Spain')>-1,True)

    def test_view_get_map(self):
        c = Client()
        r = c.get('/transformer/entry/12188/map')
        self.assertEqual(r.content.decode('utf-8').find('2.1773')>-1,True)

    def test_view_get_reviews(self):
        c = Client()
        r = c.get('/transformer/entry/12188/reviews')
        self.assertEqual(r.content.decode('utf-8').find('traditional')>-1,True)

class ToolsTestCase(TestCase):
    def test_get_entry_by_id(self):
        entry = get_entry_by_id(12188)
        entry.set_obj()
        self.assertEqual(entry.obj['name'], 'Gopal')

    def test_get_entry_by_id_force(self):
        entry = get_entry_by_id(12188)
        entry = get_entry_by_id(12188, force=True)
        entry.set_obj()
        self.assertEqual(entry.obj['name'], 'Gopal')

    def test_get_region_by_id(self):
        region = get_region_by_id(66)
        region.set_obj()
        self.assertEqual(region.obj['name'], 'Spain')

    def test_get_region_by_id_force(self):
        region = get_region_by_id(66, force=True)
        region.set_obj()
        self.assertEqual(region.obj['name'], 'Spain')