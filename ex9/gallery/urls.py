from django.urls import path

from .views import (

)


app_name = 'gallery'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
]
