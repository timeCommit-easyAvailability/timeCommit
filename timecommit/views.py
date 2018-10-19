from django.shortcuts import render


def home_view(request):
    return render(request, 'base/home.html')


def about_view(request):
    return render(request, 'base/about.html')


def register_view(request):
    return render(request, 'django_registration/registration_form.html')
