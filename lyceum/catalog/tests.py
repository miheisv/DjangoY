from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError

from .models import Category, Item, Tag


class FirstModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=150
        )
        cls.tag = Tag.objects.create(
            is_published=True,
            name='Тестовый тег',
            slug='test-tag-slug'
        )

    def test_unable_create_one_letter(self):
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = Item(
                name='Тестовый товар',
                category=self.category,
                text='test desription lol'
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_able_create_one_letter(self):
        item_count = Item.objects.count()
        self.item = Item(
            name='Тестовый товар',
            category=self.category,
            text='test превосходно'
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count + 1)


class SecondModelsTests(TestCase):
    def test_unable_create_one_category_negative_weight(self):
        category_count = Category.objects.count()

        with self.assertRaises(ValidationError):
            self.category = Category(
                is_published=True,
                name='Тестовая категория1',
                slug='test-category-slug1',
                weight=-100
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(Category.objects.count(), category_count)

    def test_unable_create_one_category_big_weight(self):
        category_count = Category.objects.count()

        with self.assertRaises(ValidationError):
            self.category = Category(
                is_published=True,
                name='Тестовая категория2',
                slug='test-category-slug2',
                weight=40000
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(Category.objects.count(), category_count)

    def test_able_create_one_category(self):
        category_count = Category.objects.count()
        self.category = Category(
            is_published=True,
            name='Тестовая категория3',
            slug='test-category-slug3',
            weight=100
        )
        self.category.full_clean()
        self.category.save()
        self.assertEqual(Category.objects.count(), category_count + 1)


class ThirdPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=150
        )
        cls.tag = Tag.objects.create(
            is_published=True,
            name='Тестовый тег',
            slug='test-tag-slug'
        )

    def test_able_giving_to_homapage(self):
        item_count = Item.objects.published_home().count()
        self.item = Item(
            name='Тестовый товар',
            category=self.category,
            text='test desription lol роскошно',
            is_on_main=True
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        items = Item.objects.published_home()

        self.assertEqual(items.count(), item_count + 1)


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=150
        )
        cls.tag = Tag.objects.create(
            is_published=True,
            name='Тестовый тег',
            slug='test-tag-slug'
        )

    # item_list 'catalog/' test
    def test_catalog_detail(self):
        response = Client().get(path='/catalog/')
        self.assertEqual(response.status_code, 200)

    # item_detail 'catalog/123' test
    def test_homepage_detail_num(self):
        self.item = Item(
            name='Тестовый товар',
            category=self.category,
            text='test превосходно'
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)
        response = Client().get(reverse('catalog:item_detail', kwargs={'pk': self.item.pk, }))
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


class PageContextTests(TestCase):
    def test_homepage_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 0)
