from django.contrib import admin

from .models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    list_display = ('image',)
    exclude = ('cropping',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'is_public')
    list_filter = ('is_public',)
