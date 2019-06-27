"""Frontend urls."""

from django.urls import path
import frontend.views as views


urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.search_result, name="search result"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
]
