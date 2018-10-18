from django.shortcuts import render


def home_view(request):
    return render(request, 'base/home.html')


def about_view(request):
    return render(request, 'base/about.html')
