from django.urls import path
# from django.contrib import admin
from .views import (
    admin_dash,
    Company_view,
    Shift_view,
    Csv_view,
    CreateCompanyView,
    CreateShiftView,
    ApproveUserScheduleView,
)


urlpatterns = [
    path('', admin_dash, name='admin_dash'),
    path('csv_view', Csv_view, name='csv'),
    path('create_company', CreateCompanyView.as_view(), name='create_company'),
    path('create_shift', CreateShiftView.as_view(), name='shift'),
    path('shifts', ApproveUserScheduleView.as_view(), name='shifts'),
]
