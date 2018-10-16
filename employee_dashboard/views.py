from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from .admin_dashboard.models import Shift
from operator import itemgetter

def employee_dashboard_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    # calender generation logic
    all_shifts = get_list_or_404(Shift)
    days_of_the_week = {
        'sunday': [],
        'monday': [],
        'tuesday': [],
        'wednesday': [],
        'thursday': [],
        'friday': [],
        'saturday': [],
    }
    for shift in all_shifts:
        new_shift = {
            'start_time': shift.start_time, 
            'end_time': shift.end_time, 
            'employees_required': shift.employees_required, 
            'employees_needed':shift.employees_needed
        }
        days_of_the_week[shift.day.lower()].append(new_shift)

    # sorting lists of shifts by start time logic
    for day in days_of_the_week:
        days_of_the_week[day].sort(key=itemgetter('start_time'))


    selected_shift = request.user.selected_shift

    context = {
        'shift': 
        'calender': days_of_the_week,

    }

    return render(request, 'employee/employee_dashboard.html', context=context)


# def notes_detail_view(request, pk=None):
#     if not request.user.is_authenticated:
#         return redirect(reverse('login'))

#     note = get_object_or_404(Note, id=pk, user__id=request.user.id)
#     context = {
#         'note': note,
#     }

#     return render(request, 'notes/notes_detail.html', context)