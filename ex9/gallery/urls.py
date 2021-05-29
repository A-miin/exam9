from django.urls import path

from .views import (
IndexView, CreatePhotoView, PhotoUpdateView, PhotoView, PhotoDeleteView,
AlbumView
)


app_name = 'gallery'

urlpatterns = [
    path('', IndexView.as_view(), name='photo-list'),
    path('photos/<int:pk>', PhotoView.as_view(), name='photo-view'),
    path('photos/add', CreatePhotoView.as_view(), name='photo-create'),
    path('photos/<int:pk>/edit', PhotoUpdateView.as_view(), name='photo-update'),
    path('photos/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo-delete'),
    path('albums/<int:pk>', AlbumView.as_view(), name='album-view')

]
