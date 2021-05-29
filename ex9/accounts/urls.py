from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from .views import UserDetailView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/<int:pk>', UserDetailView.as_view(), name='user-detail')
]