from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import User_Schedule


class TestModelExists(TestCase):
    def test_if_user_schedule_model_exists(self):
        self.assertIsNotNone(User_Schedule)


class TestViewExists(TestCase):
    def test_if_employee_dashboard_exists(self):
        from .views import employee_dashboard_view
        self.assertIsNotNone(employee_dashboard_view)


# class TestLogin(TestCase):  # pragma: no cover
#     def test_login_view_denies_anonymous(self):
#         response = self.client.get('/', follow=True)
#         self.assertRedirects(response, '/')
#         # response = self.client.post('/accounts/login/', follow=True)
#         # self.assertRedirects(response, '/')

    def test_login_view_loads(self):
        self.client.login(email='t@t.com', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'employee_dashboard.html')

    def test_login_view_fails_blank(self):
        self.client.login(email='t@t.com', password='test')
        response = self.client.post('/accounts/login/', {})  # blank data dictionary
        self.assertFormError(response, 'form', 'username', 'This field is required.')

    def test_login_view_fails_invalid(self):
        self.client.login(username='t@t.com', password='test')
        response = self.client.post('/accounts/login/', None)  # invalid data
        self.assertFormError(response, 'form', 'username', 'This field is required.')
