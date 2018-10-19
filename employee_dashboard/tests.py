from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import User_Schedule


class TestModelExists(TestCase):
    def test_if_user_schedule_model_exists(self):
        self.assertIsNotNone(User_Schedule)


# class TestLogin(TestCase):
#     def setup(self):
#         self.request = RequestFactory()
#         self.user = User.objects.create(email='test@example.com')
#         self.user.set_password('hello')

#     def test_incorrect_login(self):
#         from .views import employee_dashboard_view
#         request = self.request.get('')
#         response = employee_dashboard_view(request, self.user)
#         self.assertContains(b'Please enter a correct username and password.', response.content)


class TestLogin(TestCase):
    def test_login_view_denies_anonymous(self):
        response = self.client.get('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')
        response = self.client.post('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')

    def test_login_view_loads(self):
        self.client.login(email='t@t.com', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/url/to/view')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'employee_dashboard.html')

    def test_login_view_fails_blank(self):
        self.client.login(email='t@t.com', password='test')
        response = self.client.post('/url/to/view', {})  # blank data dictionary
        self.assertFormError(response, 'form', 'some_field', 'This field is required.')
        # etc. ...

    def test_login_view_fails_invalid(self):
        self.client.login(username='t@t.com', password='test')
        response = self.client.post('/url/to/view', None)  # blank data dictionary
        self.assertFormError(response, 'form', 'some_field', 'This field is required.')

