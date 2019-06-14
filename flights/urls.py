from django.urls import path
from .views import FlightBooking


urlpatterns = [
    path('booking/<int:flight_pk>', FlightBooking.as_view(), name="flight booking"),
]
