from django.forms import ModelForm
from .models import Shift, Company
from employee_dashboard.models import User_Schedule


class ShiftForm(ModelForm):
    """ the shift model will have these fields: day, start and end time, how many employees required and assigned
    """
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
    """the company model will have these fields:company name, address and contact email
    """
    class Meta:
        model = Company
        fields = [
            'company_name',
            'address',
            'contact_email'
            ]


class UserScheduleForm(ModelForm):
    class Meta:
        """the user schedule model will have this field: status
        """
        model = User_Schedule
        fields = [
            'status'
        ]
