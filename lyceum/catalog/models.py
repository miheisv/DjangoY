from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

from Core.models import NameMixInModel, SlugMixInModel
from Core.models import PublishedMixInModel
from catalog import validators

User = get_user_model


class Category(NameMixInModel, SlugMixInModel, PublishedMixInModel):
    weight = models.IntegerField(
        default=100,
        verbose_name='Рейтинг товара',
        help_text='Рейтинг товара, в интервале (0,32767)',
        validators=[validators.validate_weight_range])
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(NameMixInModel, SlugMixInModel, PublishedMixInModel):
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Item(PublishedMixInModel, NameMixInModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Выберите одну категорию товара'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='items',
        verbose_name='Теги',
        help_text='Выберите не менее одного тега товара'
    )
    text = models.TextField(
        validators=[validators.validate_item_need],
        verbose_name='Описание товара',
        help_text='Введите описание товара, состоящее не '
        'менее чем из двух слов, содержающее "превосходно" или "роскошно"')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
