from django.test import TestCase, Client


class StaticURLTests(TestCase):
    # endpoind url test
    def test_homepage(self):
        response = Client().get(path='/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_num(self):
        response = Client().get(path='/123')
        self.assertEqual(response.status_code, 404)

    def test_homepage_str(self):
        response = Client().get(path='/abc')
        self.assertEqual(response.status_code, 404)

    def test_homepage_numstr(self):
        response = Client().get(path='/123abc')
        self.assertEqual(response.status_code, 404)

    def test_homepage_strnum(self):
        response = Client().get(path='/abc123')
        self.assertEqual(response.status_code, 404)
