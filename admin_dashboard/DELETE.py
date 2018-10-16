from .models import Shift, Company, Scheduler
from employee_dashboard.models import User_Schedule


def shift_object():
    shift = Shift.objects.all()
    # Start time is from shift.start_time
    # Start time is from shift.end_time
    return shift


def comp_object():
    comp = Company.objects.filter(company_name ='', address='')
    # Location is the company name and address
    return comp


def sched_object():
    sched = User_Schedule.objects.all()
    # Start Date is from User_schedule.date_added
    # Subject is the user from User_Schedule.user
    return sched




*Subject, *Start Date, *Start Time, *End Time, *Location
