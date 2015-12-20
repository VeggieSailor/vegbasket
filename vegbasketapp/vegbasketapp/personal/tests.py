from django.test import TestCase

# Create your tests here.
from django.test import TestCase

import datetime
import json

from httpretty import HTTPretty

from social.p3 import urlencode
from social.actions import do_disconnect

from social.tests.models import User
from social.tests.backends.oauth import OAuth1Test, OAuth2Test
from social.tests.backends.open_id import OpenIdTest, OpenIdConnectTestMixin


# Test take from: https://github.com/omab/python-social-auth/blob/master/social/tests/backends/test_google.py
class GoogleOAuth2Test(OAuth2Test):
    backend_path = 'social.backends.google.GoogleOAuth2'
    user_data_url = 'https://www.googleapis.com/plus/v1/people/me'
    expected_username = 'foo'
    access_token_body = json.dumps({
        'access_token': 'foobar',
        'token_type': 'bearer'
    })
    user_data_body = json.dumps({
        'aboutMe': 'About me text',
        'cover': {
            'coverInfo': {
                'leftImageOffset': 0,
                'topImageOffset': 0
            },
            'coverPhoto': {
                'height': 629,
                'url': 'https://lh5.googleusercontent.com/-ui-GqpNh5Ms/'
                       'AAAAAAAAAAI/AAAAAAAAAZw/a7puhHMO_fg/photo.jpg',
                'width': 940
            },
            'layout': 'banner'
        },
        'displayName': 'Foo Bar',
        'emails': [{
            'type': 'account',
            'value': 'foo@bar.com'
        }],
        'etag': '"e-tag string"',
        'gender': 'male',
        'id': '101010101010101010101',
        'image': {
            'url': 'https://lh5.googleusercontent.com/-ui-GqpNh5Ms/'
                   'AAAAAAAAAAI/AAAAAAAAAZw/a7puhHMO_fg/photo.jpg',
        },
        'isPlusUser': True,
        'kind': 'plus#person',
        'language': 'en',
        'name': {
            'familyName': 'Bar',
            'givenName': 'Foo'
        },
        'objectType': 'person',
        'occupation': 'Software developer',
        'organizations': [{
            'name': 'Org name',
            'primary': True,
            'type': 'school'
        }],
        'placesLived': [{
            'primary': True,
            'value': 'Anyplace'
        }],
        'url': 'https://plus.google.com/101010101010101010101',
        'urls': [{
            'label': 'http://foobar.com',
            'type': 'otherProfile',
            'value': 'http://foobar.com',
        }],
        'verified': False
    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()

    def test_with_unique_user_id(self):
        self.strategy.set_settings({
            'SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID': True,
        })
        self.do_login()
