from django.urls import path
from .views import FlightBooking, SearchFlight
from .background_jobs import report


urlpatterns = [
    path('booking/', FlightBooking.as_view(), name="flight booking"),
    path('search/', SearchFlight.as_view(), name="Search flight"),
    path('report/', report, name='report')
]
