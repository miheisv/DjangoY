from django.db import models


class Feedback(models.Model):
    text = models.TextField(
        default='',
        help_text='Введите текст'
    )

    email = models.EmailField(
        help_text='Введите почту'
    )

    created_on = models.DateTimeField(
        'Дата',
        help_text='Дата создания фидбека',
        auto_now_add=True
    )

    def __str__(self):
         return 'Заявка от {}'.format(self.created.astimezone(tz).strftime('%d.%m.%Y %H:%M'))
