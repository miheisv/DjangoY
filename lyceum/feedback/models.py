from django.db import models
from django import forms


class Feedback(models.Model):
    text = models.TextField(help_text='Введите текст')

    created_on = models.DateTimeField(
        'Дата',
        help_text='Дата создания фидбека',
        auto_now_add=True
    )


class FormFromFeedback(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Feedback
        fields = '__all__'
        help_text = {
            Feedback.text.field.help_text: 'Введите текст'
        }
        labels = {
            Feedback.text.field.name: 'Текст'
        }
