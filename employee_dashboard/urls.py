from django.urls import path
from .views import employee_dashboard_view

# routing for path. this one will go to the employee dashboard view
urlpatterns = [
    path('', employee_dashboard_view, name='schedules'),
]
