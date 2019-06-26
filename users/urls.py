"""Users urls."""

from django.urls import path
from .views import LoginView, RegisterView, UserProfile


urlpatterns = [
    path('login/', LoginView.as_view(), name="auth-login"),
    path('register/', RegisterView.as_view(), name="auth-register"),
    path('profile/', UserProfile.as_view(), name="user profile")
]
