from django.contrib import admin
from .models import Photo, Album
# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    fields = ['id','photo', 'title', 'created_at','author','album','is_private','favorite']
    readonly_fields = ['id', 'created_at']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']
    fields = ['id', 'name', 'description', 'author', 'created_at', 'is_private', 'favorite']
    readonly_fields = ['id','created_at']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)

