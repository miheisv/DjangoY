from django.db import models
from django.core.validators import validate_slug


class NameMixInModel(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=150, default='standartname')


class SlugMixInModel(models.Model):
    class Meta:
        abstract = True
    slug = models.CharField(
                        max_length=200,
                        unique=True,
                        validators=[validate_slug]
                        )


class PublishedMixInModel(models.Model):
    class Meta:
        abstract = True
    is_published = models.BooleanField(default=True)
