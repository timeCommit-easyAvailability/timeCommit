from django.shortcuts import render
from .models import Shift, Company


def Company_view(request):
    company = Company.objects.all()

    context = {
        'models': company
    }
    return render(request, 'admin/admin_dashboard.html', context=context)


def Shift_view(request):
    shifts = Shift.objects.all()

    context = {
        'models': shifts
    }
    return render(request, 'dash/admin_dashboard.html', context=context)
