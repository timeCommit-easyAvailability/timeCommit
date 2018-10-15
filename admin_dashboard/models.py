from django.contrib.postgres.fields import ArrayField
from django.db import models


class Shift(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shedule_settings')
    DAY = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    day = models.CharField(choices=DAY, max_length=9, default='Monday')
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    employees_required = models.IntegerField()
    employees_assigned = ArrayField(models.IntegerField())
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    # def add_employee(self, employee_id):
    #     return self.employees_assigned.append(employee_id)

    # def remove_employee(self, employee_id):
    #     try:
    #         return self.employees_assigned.remove(employee_id)
    #     except ValueError as ve:
    #         return (ve)

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
        return '{} | {} | {}'.format(self.company_name, self.address, self.contact_email)
