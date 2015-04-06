from django.test import TestCase
from django.test import Client

class PicutreTestCase(TestCase):

    # def test_create_user(self):
    #     from picupwebapp.picture.models  import Picture, Gallery
    #     from django.contrib.auth.models import User
    #     u = User(username="test")
    #     u.save()
    #     self.assertEqual(u.id>0,True)

    def test_home_page(self):
        c = Client()
        r = c.get('/')
        self.assertEqual(r.content.decode('utf-8').find('vegan')>-1,True)
