from urllib import response
from django.test import TestCase, Client

class StaticURLTests(TestCase):
    #endpoind url test
    def tets_homepage_endpoint(self):
        response = Client.get('/')
        self.assertEqual(response.status_code, 200)
