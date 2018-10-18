from django.test import TestCase, RequestFactory
import pytest
# Create your tests here.


# # going to a different path will show a status 404
# class TestStatus404ForUnregisteredView(TestCase):


# class TestShiftModel(TestCase):
#     #user logs in
#     def setUp(self):
#         self.user = User.objects.create(username='test', email='test@example.com')
#         self.user.set_password('hello')

#         self.note = Note.objects.create(
#             title='Feed the cat',
#             description='She is hangry',
#             user=self.user
#         )

#         Note.objects.create(title='blarp', description='wat stick', user=self.user)
#         Note.objects.create(title='Gnarf', description='wat dat', user=self.user)

#     #picks a shift
#     def test_note_titles(self):
#         self.assertEqual(self.note.title, 'Feed the cat')

#     def test_note_detail(self):
#         note = Note.objects.get(title='Gnarf')

#         self.assertEqual(note.description, 'wat dat')
