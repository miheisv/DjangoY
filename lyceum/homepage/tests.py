from django.test import TestCase, Client


class StaticURLTests(TestCase):
    #endpoind url test
    def test_homepage_endpoint(self):
        response = Client.get('/')
        self.assertEqual(response.status_code, 200)
