from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day = models.DateField(verbose_name='День рождения', null=True, blank=True)

    def __str__(self):
        return 'Профиль'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Registration(models.Model):
    login = models.CharField(max_length=40,
        default='',
        help_text='Введите логин'
    )

    password = models.CharField(
        default='',
        verbose_name='Пароль',
        help_text='Введите пароль',
        max_length=64
    )
