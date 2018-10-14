from django.shortcuts import render
from .models import Schedules, Company


def Company_view(request):
    company = Company.objects.all()

    context = {
        'models': company
    }
    return render(request, 'admin/admin_dashboard.html', context=context)


def Schedule_view(request):
    schedules = Schedules.objects.all()

    context = {
        'models': schedules
    }
    return render(request, 'admin/admin_dashboard.html', context=context)
