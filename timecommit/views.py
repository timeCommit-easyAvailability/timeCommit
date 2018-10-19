from django.shortcuts import render


def home_view(request):
    """Returns the home view
    """
    return render(request, 'base/home.html')


def about_view(request):
    """Returns the About page view
    """
    return render(request, 'base/about.html')
