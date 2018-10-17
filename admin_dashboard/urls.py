from django.urls import path
from .views import Company_view, Shift_view, Csv_view


urlpatterns = [
    path('shift', Shift_view, name='shift'),
    path('csv_view', Csv_view, name='csv'),
]
