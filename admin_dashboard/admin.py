from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportActionModelAdmin
from import_export import widgets, fields, resources
from djqscsv import render_to_csv_response, write_csv
from .models import Shift, Company, Scheduler
from employee_dashboard.models import User_Schedule


@admin.register(Shift)
class ShiftAdmin(ExportMixin, admin.ModelAdmin):
    pass


@admin.register(Company)
class CompAdmin(ExportMixin, admin.ModelAdmin):
    pass


@admin.register(User_Schedule)
class ScheduleAdmin(ExportMixin, admin.ModelAdmin):
    pass


@admin.register(Scheduler)
class UserAdmin(ImportExportActionModelAdmin):
    class Meta:
        model = Scheduler
        # include = ('subject', 'start_date', 'description')
        exclude = ('id')
