from django.urls import path, include

from api.views import FavPhoto, FavAlbum, UnFavPhoto, UnFavAlbum,get_token_view



urlpatterns = [
    path('favphoto/', FavPhoto, name='photo'),
    path('favalbum/', FavAlbum, name='album'),
    path('unfavphoto/', UnFavPhoto, name='unphoto'),
    path('unfavalbum/', UnFavAlbum, name='unalbum'),
    path('token/', get_token_view, name='token'),
]
