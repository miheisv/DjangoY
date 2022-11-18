from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail, delete
from django_cleanup.signals import cleanup_pre_delete
from tinymce import models as tinymce_models


from Core.models import NameMixInModel, SlugMixInModel
from Core.models import PublishedMixInModel
from catalog import validators


class ItemManger(models.Manager):
    def published_home(self):
        return (
            self.get_queryset()
            .filter(
                is_on_main=True,
                category__is_published=True
            )
            .select_related('category')
            .order_by('name')
            .prefetch_related(
                models.Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
            )
            .only('name', 'category', 'text', 'preview', 'tags')
        )

    def published_catalog(self):
        return (
            self.get_queryset()
            .filter(
                is_on_main=True,
                category__is_published=True
            )
            .select_related('category')
            .order_by('category')
            .prefetch_related(
                models.Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
            )
            .only('name', 'category', 'text', 'preview', 'tags')
        )


class Category(NameMixInModel, SlugMixInModel, PublishedMixInModel):
    objects = ItemManger()
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
    objects = ItemManger()

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
    text = tinymce_models.HTMLField(
        validators=[validators.validate_item_need('превосходно', 'роскошно')],
        verbose_name='Описание товара',
        help_text='Введите описание товара, состоящее не '
        'менее чем из двух слов, содержающее "превосходно" или "роскошно"'
    )
    is_on_main = models.BooleanField(default=False, verbose_name='Флаг')

    def short_text(self):
        return ' '.join(self.text.split()[:10])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Preview(models.Model):
    upload = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='Превью',
        help_text='Главное изображение товара'
    )
    item = models.OneToOneField(
        Item,
        verbose_name='Товар',
        on_delete=models.CASCADE,
        primary_key=True,
        help_text='Выбранный товар'
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Изображение отсутствует'

    image_tmb.short_description = 'Превью'
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = 'Превью'
        verbose_name_plural = 'Превьюшечки'


class PhotoGallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/gallery/%Y/%m',
        verbose_name='Изображение товара',
        help_text='Загрузите изображение товара'
    )
    item = models.ForeignKey(
        Item,
        verbose_name='Товар',
        on_delete=models.CASCADE,
        help_text='Выбранный товар'
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Изображение отсутствует'

    image_tmb.short_description = 'Галлерея'
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлереи'
