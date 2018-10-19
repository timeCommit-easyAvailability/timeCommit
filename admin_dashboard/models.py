from django.contrib.postgres.fields import ArrayField
# from django.contrib.auth.models import User
from django.db import models


class Shift(models.Model):
    """this is the shift model. Each shift will take on this form
    """
    # days of the week
    DAY = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    # properties and how they are displayed and what data form they take e.g. employees required field is an integer
    day = models.CharField(choices=DAY, max_length=9, default='Monday')
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    employees_required = models.IntegerField()
    employees_assigned = ArrayField(models.IntegerField(), null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Shift Day: {} | Start: {} | End: {} | Volunteers Required: {} | Volunteers: {}>'.format(
            self.day,
            self.start_time,
            self.end_time,
            self.employees_required,
            self.employees_assigned
            )

    def __str__(self):
        return 'Day: {} | Start time: {} | End Time: {}'.format(
            self.day,
            self.start_time,
            self.end_time
            )


class Company(models.Model):
    """this is the company model. Each company will take on this form
    """
    company_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    contact_email = models.EmailField(max_length=254)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Company Name: {} | Address: {} | Contact Email: {}>'.format(
            self.company_name,
            self.address,
            self.contact_email
            )

    def __str__(self):
        return '{} | {} | {}'.format(
            self.company_name,
            self.address,
            self.contact_email
        )


class Scheduler(models.Model):
    """this is the scheduler model. each scheduler will take on this form
    """
    subject = models.CharField(max_length=254)
    start_date = models.DateField()
    description = models.CharField(max_length=254)

    def __repr__(self):
        return 'Subject {} | Start Date: {} | Description: {}'.format(
            self.subject,
            self.start_date,
            self.description
            )

    def __str__(self):
        return '{} {} {}'.format(
            self.subject,
            self.description,
            self.start_date
            )
