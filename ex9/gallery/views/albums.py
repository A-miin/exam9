from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode

from gallery.models import Photo, Album
from gallery.forms import AlbumForm


class AlbumView(DetailView):
    model = Album
    template_name = 'album/view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(album = self.object).exclude(is_private=True)
        context['is_author']=self.object.author==self.request.user
        return context

#
class CreateAlbumView(LoginRequiredMixin, CreateView):
    template_name = 'album/create.html'
    form_class = AlbumForm
    model = Album
    success_url = reverse_lazy('gallery:photo-list')

    def form_valid(self, form):
        self.album = form.save(commit=False)
        self.album.author = self.request.user
        self.album.save()
        form.save_m2m()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('gallery:album-view', pk = self.album.id)


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    model = Album
    template_name = 'album/update.html'
    context_object_name = 'album'
    permission_required = 'gallery.change_album'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def get_success_url(self):
        return reverse('gallery:album-view', kwargs={'pk': self.kwargs.get('pk')})


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = 'partial/delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy("gallery:photo-list")
    permission_required = 'gallery.delete_album'
    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

