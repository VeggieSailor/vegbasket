from django.test import TestCase
from django.test import Client

class HomeTestCase(TestCase):
    def test_login_page(self):
        c = Client()
        r = c.get('/')
        self.assertEqual(r.content.find('Veggie Sailor')>-1,True)
