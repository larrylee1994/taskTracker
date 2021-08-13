from django.contrib import admin
from main.models import Worksheet, Entry
from import_export import resources
from import_export.widgets import TimeWidget
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.admin import DateFieldListFilter, ListFilter


class EntryResource(resources.ModelResource):

    name = Field(attribute='worksheet__user__first_name', column_name='NAME')
    store = Field(attribute='store', column_name='STORE')
    operation = Field(attribute='operation', column_name='OPERATION')
    date = Field(
        column_name='DAY',
        attribute='worksheet__date',
        widget=TimeWidget(format='%A'))
    # DEMO leading 0 in front of hour
    start_time = Field(
        column_name='START TIME',
        attribute='start_time',
        widget=TimeWidget(format='%-I:%M:%S %p'))
    end_time = Field(
        column_name='END TIME',
        attribute='end_time',
        widget=TimeWidget(format='%-I:%M:%S %p'))

    class Meta:
        model = Entry
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'date', 'store',
                  'operation', 'start_time', 'end_time')
        export_order = fields


class EntryAdmin(ImportExportActionModelAdmin):
    resource_class = EntryResource
    view_on_site = True
    list_display = ('get_name', 'get_date', 'store',
                    'operation', 'start_time', 'end_time')

    list_filter = (
        ('worksheet__date', DateFieldListFilter),
    )

    def get_name(self, obj):
        first_name = obj.worksheet.user.first_name
        last_name = obj.worksheet.user.last_name
        return (f"{last_name}, {first_name}")

    def get_date(self, obj):
        return obj.worksheet.date

    def get_day(self, obj):

        return obj.worksheet.date

    get_name.admin_order_field = 'worksheet__user__last_name'
    get_name.short_description = 'Name'
    get_date.admin_order_field = 'worksheet__id'
    get_date.short_description = 'Date'


class WorksheetAdmin(admin.ModelAdmin):

    list_display = ('get_name', 'get_date')
    list_filter = (
        ('date', DateFieldListFilter),
    )

    def get_name(self, obj):
        first_name = obj.user.first_name
        last_name = obj.user.last_name
        return (f"{last_name}, {first_name}")

    def get_date(self, obj):
        return obj.date

    get_name.admin_order_field = 'user__last_name'
    get_name.short_description = 'Name'
    get_date.admin_order_field = 'id'
    get_date.short_description = 'Date'


admin.site.register(Worksheet, WorksheetAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.site_header = 'Family administration'
