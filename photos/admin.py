from django.contrib import admin

from .models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    list_display = ('image',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_filter = ('is_public',)
