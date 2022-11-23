from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django import forms

from feedback.models import FormFromFeedback, Feedback


class BaseTestCase(TestCase):
    def check_fields_in_object(
        self, 
        object,
        must_loaded_keys,
        prefetched_keys,
        must_not_loaded_keys
    ):
        if must_loaded_keys != None:
            for must_loaded_key in must_loaded_keys:
                self.assertIn(must_loaded_key, object.__dict__)
        if prefetched_keys != None:
            for prefetched_key in prefetched_keys:
                self.assertIn(prefetched_key, object.__dict__['_prefetched_objects_cache'])
        if must_not_loaded_keys != None:
            for must_not_loaded_key in must_not_loaded_keys:
                self.assertNotIn(must_not_loaded_key, object.__dict__)


class TestCatalogPage(BaseTestCase):
    fiхtures = ['fixtures.json']
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FormFromFeedback()

    def test_feedback_show_correct_item(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertEqual(response.status_code, 200)

    def test_feedback_contains_items(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_feedback_items_db_fields(self):
        response = Client().get(reverse('feedback:feedback'))
        for item in response.context['form']:
            self.check_fields_in_object(
                item,
                ('label', 'help_text', ),
                None,
                None,
            )

    def test_form_label(self):
        new_label = TestCatalogPage.form.fields['text'].label
        self.assertEqual(new_label, 'Текст')
        new_label = TestCatalogPage.form.fields['email'].label
        self.assertEqual(new_label, 'Почта')
    def test_form_help_text(self):
        new_help_text = TestCatalogPage.form.fields['text'].help_text
        self.assertEqual(new_help_text, 'Введите текст')
        new_help_text = TestCatalogPage.form.fields['email'].help_text
        self.assertEqual(new_help_text, 'Введите почту')

    def test_redirect_feedback(self):
        feedback_count = Feedback.objects.count()
        form_data = {
            'text': 'Тест',
            'email': 'example@yandex.ru',
        }
        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, reverse('feedback:feedback'))
        self.assertEqual(Feedback.objects.count(), feedback_count + 1)
