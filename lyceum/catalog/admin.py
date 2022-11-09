from django.contrib import admin
from catalog.models import Item, Category, Tag, Preview, PhotoGallery


class PreviewInline(admin.TabularInline):
    model = Preview
    extra = 0
    readonly_fields = ('image_tmb',)
    fields = ('image_tmb',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'preview')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    inlines = [
        PreviewInline,
    ]
    filter_horizontal = ('tags',)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')


@admin.register(Preview)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')


admin.site.register(Category)
admin.site.register(Tag)
