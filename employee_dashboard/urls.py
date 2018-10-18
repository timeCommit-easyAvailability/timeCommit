from django.urls import path
from .views import User_Schedule_view

urlpatterns = [
    path('', User_Schedule_view, name='schedules'),
]
