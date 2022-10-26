from django.test import TestCase, Client


class StaticURLTests(TestCase):

    # endpoind url test
    def test_homepage_endpoint(self):
        response = Client.get('/')
        self.assertEqual(response.status_code, 200)

    # endpoind url test
    def test_homepage_endpoin(self):
        response = Client.get('/catalog/')
        self.assertEqual(response.status_code, 200)

    # endpoind url test
    def test_homepage_endpoi(self):
        response = Client.get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

    # endpoind url test
    def test_homepage_endpo(self):
        response = Client.get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)

    # endpoind url test
    def test_homepage_endp(self):
        response = Client.get('/catalog/abc1/')
        self.assertEqual(response.status_code, 404)

    # endpoind url test
    def test_homepage_end(self):
        response = Client.get('/catalog/1abc/')
        self.assertEqual(response.status_code, 404)
