from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from admin_dashboard.models import Shift
from .models import User_Schedule
from operator import itemgetter


def employee_dashboard_view(request):
    """if user is not authenticated, return permission denied error.
    for shift, show the days of the week. and iterate through all of the
    shifts with the start time and end time. and show the days of
    the week on the calendar. return to the employee dashboard.
    """
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

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
            'employees_assigned': shift.employees_assigned,
            'id': shift.id,
            'day': shift.day,
        }
        days_of_the_week[shift.day.lower()].append(new_shift)

    # sorting lists of shifts by start time logic
    for day in days_of_the_week:
        days_of_the_week[day].sort(key=itemgetter('start_time'))

    # handle user prefs submitted
    if 'list' in request.POST:
        decoded_prefs = request.body.decode().split('&')
        split_prefs = []
        chosen_user_prefs = []
        true_prefs = []

        for i in decoded_prefs:
            split_prefs.append(i.split('='))
        for i in split_prefs:
            chosen_user_prefs.append(i)

        chosen_user_prefs.pop(0)
        chosen_user_prefs.pop(-1)

        for i in chosen_user_prefs:
            if i[1]:
                true_prefs.append(i)

        true_prefs = dict(true_prefs)

        # create the User_Schedule from prefs
        for key, values in true_prefs.items():
            selected_shift = get_object_or_404(Shift, pk=key)
            user_schedule_instance = User_Schedule.objects.create(
                user=request.user,
                selected_shift=selected_shift,
                priority=values)

            user_schedule_instance.save()

    context = {
        'calendar': days_of_the_week,
        # 'all_projects': all_shifts

    }

    return render(request, 'employee/employee_dashboard.html', context=context)
