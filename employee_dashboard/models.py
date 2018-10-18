from django.db import models
from django.contrib.auth.models import User
from admin_dashboard.models import Shift


class User_Schedule(models.Model):
    PRIORITY = [
        (1, 'Highest'),
        (2, 'Medium'),
        (3, 'Lowest'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='schedule_settings'
        )

    selected_shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY, default=3)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('user', 'selected_shift',)
        # unique_together = ('user', 'priority',)

    def __repr__(self):
        return '<Shift: {} | Priority: {} | Status: {} | User: {} >'.format(
            self.selected_shift,
            self.priority,
            self.status,
            self.user,
            )

    def __str__(self):
        return '{} | {} | {}'.format(self.selected_shift, self.user, self.status)



