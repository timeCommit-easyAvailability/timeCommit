from django.urls import path
from .views import employee_dashboard_view

urlpatterns = [
    path('', employee_dashboard_view, name='schedules'),
]

