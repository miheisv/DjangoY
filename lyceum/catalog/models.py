from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model

from Core.models import NameMixInModel, SlugMixInModel
from Core.models import PublishedMixInModel
from . import validators

User = get_user_model


class Category(NameMixInModel, SlugMixInModel, PublishedMixInModel):
    weight = models.IntegerField(
        default=100, 
        validators=[validators.validate_weight_range])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(NameMixInModel, SlugMixInModel, PublishedMixInModel):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(NameMixInModel, PublishedMixInModel):
    text = models.TextField(validators=[validators.validate_item_need])
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tag)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'