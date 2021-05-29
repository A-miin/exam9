from django.urls import path

from .views import (
IndexView, CreatePhotoView, PhotoUpdateView, PhotoView, PhotoDeleteView
)


app_name = 'gallery'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
]
