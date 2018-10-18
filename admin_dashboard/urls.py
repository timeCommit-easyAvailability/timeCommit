from django.urls import path
# from django.contrib import admin
from .views import (
    Company_view,
    Shift_view,
    Csv_view,
    CreateCompanyView,
    CreateShiftView,
    ApproveUserScheduleView,
)


urlpatterns = [
    # path('shift', Shift_view, name='shift'),
    path('csv_view', Csv_view, name='csv'),
    # path('csv_view/<int:pk>', Csv_view, name='csv_pk'),
    path('create_company', CreateCompanyView.as_view(), name='create_company'),
    path('create_shift', CreateShiftView.as_view(), name='shift'),
    # path('approve/<int:id>', ApproveUserScheduleView.as_view(), name='approve'),
    path('shifts', ApproveUserScheduleView.as_view(), name='shifts'),
]
