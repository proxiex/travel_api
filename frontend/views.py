from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def search_result(request):
    return render(request, 'search_result.html')
