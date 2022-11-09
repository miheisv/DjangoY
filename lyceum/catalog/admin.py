from django.contrib import admin
from catalog.models import Item, Category, Tag, Preview, PhotoGallery


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'preview')
    list_editable = ('is_published',)
    list_display_links = ('name',)

    filter_horizontal = ('tags',)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'gallery')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Preview)
