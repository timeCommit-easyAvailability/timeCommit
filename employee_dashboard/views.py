from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from admin_dashboard.models import Shift
from operator import itemgetter


def employee_dashboard_view(request):
    """if user is not authenticated, return permission denied error.
    for shift, show the days of the week. and iterate through all of the
    shifts with the start time and end time. and show the days of
    the week on the calendar. return to the employee dashboard.
    """
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
            'employees_assigned': shift.employees_assigned
        }
        days_of_the_week[shift.day.lower()].append(new_shift)

    # sorting lists of shifts by start time logic
    for day in days_of_the_week:
        days_of_the_week[day].sort(key=itemgetter('start_time'))

    context = {
        'calendar': days_of_the_week,
        # 'all_projects': all_shifts

    }

    return render(request, 'employee/employee_dashboard.html', context=context)
