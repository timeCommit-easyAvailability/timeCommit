from django.urls import path
from .views import Company_view, Schedule_view

urlpatterns = [
    path('', Schedule_view, name='schedules'),
]
