from urllib import response
from django.test import TestCase, Client

class StaticURLTests(TestCase):
    #endpoind url test
    def tets_homepage_endpoint(self):
        response = Client.get('/')
        self.assertEqual(response.status_code, 200)
    
        #endpoind url test
    def tets_homepage_endpoint(self):
        response = Client.get('/catalog/')
        self.assertEqual(response.status_code, 200)
    
        #endpoind url test
    def tets_homepage_endpoint(self):
        response = Client.get('/catalog/0/')
        self.assertEqual(response.status_code, 404)
    
        #endpoind url test
    def tets_homepage_endpoint(self):
        response = Client.get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)
    
            #endpoind url test
    def tets_homepage_endpoint(self):
        response = Client.get('/catalog/abc1/')
        self.assertEqual(response.status_code, 404)
    
            #endpoind url test
    def tets_homepage_endpoint(self):
        response = Client.get('/catalog/1abc/')
        self.assertEqual(response.status_code, 404)
