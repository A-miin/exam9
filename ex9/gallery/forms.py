from django import forms
from django.contrib.auth.models import User

from .models import Photo, Album

class PhotoForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), label='Альбом', required=False)

    def __init__(self, user, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album'] = forms.ModelChoiceField(queryset=Album.objects.filter(author=user),  label='Альбом', required=False)

    class Meta:
        model=Photo
        fields=('photo', 'title', 'album')


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields=('name', 'description', 'is_private')