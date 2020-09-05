from django.shortcuts import render


def index(request):
    """
    index
    """
    return render(request, 'frontend/index.html')
