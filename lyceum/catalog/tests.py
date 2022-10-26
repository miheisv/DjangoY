from django.test import TestCase, Client


class StaticURLTests(TestCase):

    # item_list test
    def test_catalog_list(self):
        response = Client().get(path='/')
        self.assertEqual(response.status_code, 200)

    # item_detail 'catalog/' test
    def test_catalog_detail(self):
        response = Client().get(path='/catalog/')
        self.assertEqual(response.status_code, 200)

    # item_detail 'catalog/123' test
    def test_homepage_detail_num(self):
        response = Client().get(path='/catalog/123')
        self.assertEqual(response.status_code, 200)

    # zero test
    def test_homepage_detail_zero(self):
        response = Client().get(path='/catalog/0/')
        self.assertEqual(response.status_code, 404)

    # negative test
    def test_homepage_detail_negative(self):
        response = Client().get(path='/catalog/-1/')
        self.assertEqual(response.status_code, 404)

    # str+int test
    def test_homepage_detail_strnum(self):
        response = Client().get(path='/catalog/abc123/')
        self.assertEqual(response.status_code, 404)

    # int+str test
    def test_homepage_detail_numstr(self):
        response = Client().get(path='/catalog/123abc/')
        self.assertEqual(response.status_code, 404)

    # dot test
    def test_homepage_detail_dot(self):
        response = Client().get(path='/catalog/1.2/')
        self.assertEqual(response.status_code, 404)
