"""Frontend views."""

from django.shortcuts import render


def index(request):
    """Home page."""
    return render(request, 'index.html')


def search_result(request):
    """Search page."""
    return render(request, 'search_result.html')
