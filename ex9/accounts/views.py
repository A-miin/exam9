from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from gallery.models import Photo, Album

# Create your views here.
class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(author=self.object).exclude(is_private=True)
        context['albums'] = Album.objects.filter(author=self.object).exclude(is_private=True)
        context['fav_photos'] = self.object.favorite_photos.all().filter(is_private=False)
        context['fav_albums'] = Album.objects.filter(favorite=self.object).exclude(is_private=True)
        if self.object==self.request.user:
            context['private_photos'] = Photo.objects.filter(author=self.object).filter(is_private=True)
            context['private_albums'] = Album.objects.filter(author=self.object).filter(is_private=True)
        return context

