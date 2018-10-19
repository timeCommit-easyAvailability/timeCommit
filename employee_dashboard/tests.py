from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import User_Schedule


class TestIfUserScheduleModelExists(TestCase):
    assert User_Schedule
