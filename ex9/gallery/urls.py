from django.urls import path

from .views import (
IndexView, CreatePhotoView, PhotoUpdateView, PhotoView, PhotoDeleteView,
AlbumView, CreateAlbumView,AlbumUpdateView,AlbumDeleteView
)


app_name = 'gallery'

urlpatterns = [
    path('', IndexView.as_view(), name='photo-list'),
    path('photos/<int:pk>', PhotoView.as_view(), name='photo-view'),
    path('photos/add', CreatePhotoView.as_view(), name='photo-create'),
    path('album/add', CreateAlbumView.as_view(), name='album-create'),
    path('photos/<int:pk>/edit', PhotoUpdateView.as_view(), name='photo-update'),
    path('album/<int:pk>/edit', AlbumUpdateView.as_view(), name='album-update'),
    path('photos/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo-delete'),
    path('album/<int:pk>/delete', AlbumDeleteView.as_view(), name='album-delete'),
    path('albums/<int:pk>', AlbumView.as_view(), name='album-view')

]
