from django.shortcuts import render

# Create your views here.
from .models import Amodel


def Amodel_view(request):
    models = Amodel.objects.all()

    context = {
        'models': models
    }
    return render(request, 'dash/admin_dashboard.html', context=context)
