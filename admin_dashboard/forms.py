from django.forms import ModelForm
from .models import Shift, Company
from employee_dashboard.models import User_Schedule


class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = [
            'day',
            'start_time',
            'end_time',
            'employees_required',
            'employees_assigned'
        ]


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'address',
            'contact_email'
            ]


class UserScheduleForm(ModelForm):
    class Meta:
        model = User_Schedule
        fields = [
            'status'
        ]
