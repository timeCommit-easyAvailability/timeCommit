from django.urls import path
from .views import Amodel_view

urlpatterns = [
    path('', Amodel_view, name='employee_dash'),
]