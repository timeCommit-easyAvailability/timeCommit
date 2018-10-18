from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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


class ApproveUserScheduleView(LoginRequiredMixin, ListView):
    template_name = 'dash/approve_shifts.html'
    model = User_Schedule
    form_class = UserScheduleForm
    success_url = reverse_lazy('dash/admin_dashboard.html')
    login_url = reverse_lazy('login')

    shifts = list(User_Schedule.objects.values(
        'selected_shift__user_schedule__user__first_name',
        'selected_shift__user_schedule__user__last_name',
        'selected_shift__day',
        'selected_shift__start_time',
        'selected_shift__end_time',
        'priority',
        'status',
        ))
    # import pdb; pdb.set_trace()

# def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
#         return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        counter = 0
        context['prefs'] = []
        for i in self.shifts:
            context['prefs'].append(dict(i))
            counter += 1

        # for i in self.shifts:
        #     context[i] += i
        # context['first_name'] = User_Schedule.objects.values('selected_shift__user_schedule__user__first_name')
        # import pdb; pdb.set_trace()
        return context



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
        )
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
