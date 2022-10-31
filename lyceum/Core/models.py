from django.db import models


class NameMixInModel(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(
        'Название', max_length=150,
        default='Стандартное название',
        help_text='до 150 символов'
    )


class SlugMixInModel(models.Model):
    slug = models.SlugField(
        'Идентификатор',
        max_length=200,
        unique=True,
        help_text='уникальное значение до 200'
        ' символов(только латинца, цифры, _ и -)'
    )

    class Meta:
        abstract = True


class PublishedMixInModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True
