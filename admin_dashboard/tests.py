from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Shift, Company, Scheduler
# Create your tests here.


class TestIfModelsExists(TestCase):
    def test_if_models_exist(self):
        self.assertIsNotNone(Shift),
        self.assertIsNotNone(Company),
        self.assertIsNotNone(Scheduler)


class TestCSVFile(TestCase):
    def test_csv_file_exists(self):
        from .views import Csv_view
        self.assertIsNotNone(Csv_view)


# class TestAdmin(TestCase):
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

# class TestAbleToCreateShifts(TestCase):

#
# class TestCompanyCreated(TestCase):


