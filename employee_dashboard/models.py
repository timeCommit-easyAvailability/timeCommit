from django.db import models
from django.contrib.auth.models import User
from admin_dashboard.models import Shift


class User_Schedule(models.Model):
    """this is the user schedule model
    """
    # priority for what the user wants on their schedule. 1 being the highest priority while 3 being of the lowest priority
    PRIORITY = [
        (1, 'Highest'),
        (2, 'Medium'),
        (3, 'Lowest'),
    ]

    # user is given foreign key of user and if they delete, everything related will also be deleted
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='schedule_settings'
        )

    # properties connected to user schedule e.g. status is a boolean which will take either true or false
    selected_shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY, default=3)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('user', 'selected_shift',)

    def __repr__(self):  # pragma: no cover
        return '<Shift: {} | Priority: {} | Status: {} | User: {} >'.format(
            self.selected_shift,
            self.priority,
            self.status,
            self.user,
            )

    def __str__(self):  # pragma: no cover
        return '{} | {} | {}'.format(
            self.selected_shift,
            self.user,
            self.status
        )
