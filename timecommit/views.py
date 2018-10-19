from django.shortcuts import render


def home_view(request):
    """Returns the home view
    """
    return render(request, 'base/home.html')


def about_view(request):
    """Returns the About page view
    """
    return render(request, 'base/about.html')


def register_view(request):
    """Returns the registration view
    """
    return render(request, 'django_registration/registration_form.html')
