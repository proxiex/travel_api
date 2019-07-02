"""Frontend views."""

from django.shortcuts import render


def index(request):
    """Home page."""
    return render(request, 'index.html')


def search_result(request):
    """Search page."""
    return render(request, 'search_result.html')


def login(request):
    """Login page."""
    return render(request, 'login.html')


def registration(request):
    """Registration page."""
    return render(request, 'registration.html')


def booking(request):
    """Booking page."""
    return render(request, 'booking.html')
