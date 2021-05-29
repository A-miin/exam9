from django.urls import path

from .views import (
IndexView, CreatePhotoView, PhotoUpdateView, PhotoView, PhotoDeleteView
)


app_name = 'gallery'

urlpatterns = [
    path('photos/', IndexView.as_view(), name='list'),
    path('photos/<int:pk>', PhotoView.as_view(), name='view'),
]
