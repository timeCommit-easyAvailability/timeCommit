from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    FormView,
    )
from django.urls import reverse_lazy
import time
import datetime
from datetime import date
from djqscsv import render_to_csv_response, write_csv
from .models import Shift, Company
from .forms import ShiftForm, CompanyForm, UserScheduleForm
from employee_dashboard.models import User_Schedule


def about_view(request):
    return render(request, 'base/about.html')


def admin_dash(request):
    return render(request, 'dash/admin_dashboard.html')


def Company_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    company = Company.objects.all()

    context = {
        'models': company
    }
    return render(request, 'dash/admin_dashboard.html', context=context)


def Shift_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    shifts = Shift.objects.all()

    context = {
        'models': shifts
    }
    return render(request, 'dash/admin_dashboard.html', context=context)


class CreateCompanyView(LoginRequiredMixin, CreateView):
    template_name = 'dash/create_company.html'
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('dash/admin_dashboard.html')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)


class CreateShiftView(LoginRequiredMixin, CreateView):
    template_name = 'dash/create_shift.html'
    model = Shift
    form_class = ShiftForm
    success_url = reverse_lazy('dash/admin_dashboard.html')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)


def approve_user_schedule_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    all_schedules = list(get_list_or_404(User_Schedule))

    schedules = []
    for schedule in all_schedules:

        new_schedule = {
            'first_name': schedule.user.first_name,
            'last_name': schedule.user.last_name,
            'shift_id': schedule.selected_shift.id,
            'start_time': schedule.selected_shift.start_time,
            'end_time': schedule.selected_shift.end_time,
            'id': schedule.id,
            'day': schedule.selected_shift.day,
            'priority': schedule.priority,
            'status': schedule.status,
            'needed': schedule.selected_shift.employees_required,
            'assigned': schedule.selected_shift.employees_assigned,
        }
        schedules.append(new_schedule)

    if 'list' in request.POST:
        decoded_schedules = request.body.decode().split('&')
        split_schedules = []
        admin_assigned_schedules = []
        # refactor inefficient declations eventually
        true_schedules = []

        for i in decoded_schedules:
            split_schedules.append(i.split('='))
        for i in split_schedules:
            admin_assigned_schedules.append(i)

        admin_assigned_schedules.pop(0)
        admin_assigned_schedules.pop(-1)

        for i in admin_assigned_schedules:
            true_schedules.append(i)

        true_schedules = dict(true_schedules)

        for key, values in true_schedules.items():

            User_Schedule.objects.filter(pk=key).update(status='True')
            user_id = User_Schedule.objects.values().filter(pk=key)[0]['user_id']
            shift_id = User_Schedule.objects.values().filter(pk=key)[0]['selected_shift_id']
            ass_emp = Shift.objects.values().filter(pk=shift_id)[0]['employees_assigned']
            if user_id not in ass_emp:
                ass_emp.append(user_id)
            else:
                raise ValueError("You can't have the same shift twice")

            Shift.objects.filter(pk=shift_id).update(employees_assigned=ass_emp)

        return HttpResponseRedirect('shifts')
    context = {
        'schedules': schedules,
    }

    return render(request, 'dash/approve_shifts.html', context=context)


def Csv_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    def get_date(shifts):
        for i in shifts:
            for keys, vals in i.items():
                if vals == 'monday':
                    s_date = next_weekday(datetime.date.today(), 0)
                    i['selected_shift__day'] = s_date
                if vals == 'tuesday':
                    s_date = next_weekday(datetime.date.today(), 1)
                    i['selected_shift__day'] = s_date
                if vals == 'wednesday':
                    s_date = next_weekday(datetime.date.today(), 2)
                    i['selected_shift__day'] = s_date
                if vals == 'thursday':
                    s_date = next_weekday(datetime.date.today(), 3)
                    i['selected_shift__day'] = s_date
                if vals == 'friday':
                    s_date = next_weekday(datetime.date.today(), 4)
                    i['selected_shift__day'] = s_date
                if vals == 'saturday':
                    s_date = next_weekday(datetime.date.today(), 5)
                    i['selected_shift__day'] = s_date
                if vals == 'sunday':
                    s_date = next_weekday(datetime.date.today(), 6)
                    i['selected_shift__day'] = s_date
        return shifts

    def next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        future_day = d + datetime.timedelta(days_ahead)
        future_day = future_day.strftime("%m/%d/%Y")
        return future_day

    # shift = get_object_or_404(User_Schedule, id=pk)
    shifts = User_Schedule.objects.values(
        'selected_shift__user_schedule__user__first_name',
        'selected_shift__day',
        'selected_shift__start_time',
        'selected_shift__end_time',
        ).distinct('id')
    get_date(shifts)
    return render_to_csv_response(shifts, field_order={
            'selected_shift__user_schedule__user__first_name'
        },
        field_header_map={
        'selected_shift__user_schedule__user__first_name': 'Subject',
        'selected_shift__day': 'Start Date',
        'selected_shift__start_time': 'Start Time',
        'selected_shift__end_time': 'End Time'
    })
