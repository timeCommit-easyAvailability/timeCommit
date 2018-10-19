from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Shift, Company, Scheduler
# Create your tests here.


class TestIfShiftModelExists(TestCase):
    assert Shift


class TestIfCompanyModelExists(TestCase):
    assert Company


class TestIfSchedulerModelExists(TestCase):
    assert Scheduler


# class TestAdmin_AdminCanLogin(TestCase):
#     # Admin logs in
#     def setUp(self):
#         self.user = User.objects.create(email='test@example.com')
#         self.user.set_password('hello')
#     # Test to see if Admin sees Admin dashboard or Admin View


# # Create your tests here.
# class TestAdmin_MemberCannotLoginAsAdmin(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(email='test@example.com')
#         self.user.set_password('hello')
    # Test to see if Member does not see Admin dashboard or Admin View


# class TestShiftModel(TestCase):

