rom django.contrib import admin
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

"""
user = fields.Field(column_name='user', attribute='user', widget=widgets.ForeignKeyWidget(settings.AUTH_USER_MODEL, 'id'))

forskningsresultater = fields.Field(
    column_name='forskningsresultater',
    attribute='forskningsresultater',
    widget=widgets.ForeignKeyWidget(Forskningsresultater,'id')
    )


from import_export import widgets, fields, resources
class PersonResResource(resources.ModelResource):
    user = fields.Field(column_name='user_id', attribute='user', widget=widgets.ForeignKeyWidget(settings.AUTH_USER_MODEL, 'id'))
    forskningsresultater = fields.Field(
    	column_name='forskningsresultater_id',
    	attribute='forskningsresultater',
    	widget=widgets.ForeignKeyWidget(Forskningsresultater, 'id')
    	)
    class Meta:
        model = PersonRes
        fields = ('id','user','forskningsresultater','participant',)

from import_export.admin import ImportExportModelAdmin
class PersonResAdmin(ImportExportModelAdmin):
    class Meta:
        resource_class: PersonResResource
admin.site.register(PersonRes,PersonResAdmin)





"""
