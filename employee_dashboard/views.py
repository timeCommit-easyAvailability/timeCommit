from django.shortcuts import render
from .models import User_Schedule


def User_Schedule_view(request):
    u_sched = User_Schedule.objects.all()

    context = {
        'models': u_sched
    }
    return render(request, 'models/models_list.html', context=context)
