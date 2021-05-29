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
from gallery.forms import PhotoForm


class IndexView(ListView):
    """
    Представление для просмотра списка статей. Представление реализовано с
    использованием generic-представления ListView.

    В представлении активирована пагинация и реализован поиск
    """
    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at')

class PhotoView(DetailView):
    model = Photo
    template_name = 'photo/view.html'


class CreatePhotoView(LoginRequiredMixin, CreateView):
    template_name = 'photo/create.html'
    form_class = PhotoForm
    model = Photo
    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):
        self.photo = form.save(commit=False)
        try:
            album = get_object_or_404(Album, id=self.kwargs.get('pk'))
            self.photo.album = album
        except:
            self.photo.album = None


        self.photo.save()
        form.save_m2m()
        return self.get_success_url()


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = PhotoForm
    model = Photo
    template_name = 'photo/update.html'
    context_object_name = 'photo'
    permission_required = 'gallery.change_photo'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def get_success_url(self):
        return reverse('photo:view', kwargs={'pk': self.kwargs.get('pk')})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'partial/delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('photo:list')
    permission_required = 'gallery.delete_photo'
