from django.urls import path
from .views import index, search_result


urlpatterns = [
    path('', index, name="index"),
    path('result/', search_result, name="search result"),
]
