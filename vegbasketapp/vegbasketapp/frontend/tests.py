from django.test import TestCase
from django.test import Client
# Create your tests here.
class ExampleEntry(TestCase):
    def test_view_get_example_entry(self):
        c = Client()
        r = c.get('/frontend/entry_example/')
        self.assertEqual(r.content.decode('utf-8').find('Hotel')>-1,True)