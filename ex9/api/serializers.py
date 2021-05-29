from rest_framework import serializers
from gallery.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'photo', 'title', 'author', 'created_at','album','is_private')
        read_only_fields = ('id', 'created_at')

class AlbumForm(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields=('id', 'name', 'description', 'is_private', 'author', 'created_at')
        read_only_fields = ('id', 'created_at')