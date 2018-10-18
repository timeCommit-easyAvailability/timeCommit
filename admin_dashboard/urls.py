from django.urls import path
from .views import Company_view, Shift_view


urlpatterns = [
    path('', Shift_view, name='shift'),
]
