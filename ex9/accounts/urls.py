from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from .views import UserDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>', UserDetailView.as_view(), name='user-detail')
]