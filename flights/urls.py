from django.urls import path
from .views import FlightBooking


urlpatterns = [
    path('booking/', FlightBooking.as_view(), name="flight booking"),
]
