from django.db import models
from django.contrib.auth.models import User
from admin_dashboard.models import Schedules


class User_Schedule(models.Model):
    PRIORITY = [
        (1, 'highest'),
        (2, 'Medium'),
        (3, 'Lowest'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shedule_settings'
        )

    shift_id = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    priotity = models.IntegerField(choices=PRIORITY, default=3)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Shift: {} | Priotity: {} | Status: {}>'.format(
            self.shift_id,
            self.priotity,
            self.status,
            )

    def __str__(self):
        return '{} | {} | {}'.format(self.shift_id, self.priotity, self.status)
