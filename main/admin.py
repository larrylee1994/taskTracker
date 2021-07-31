from django.contrib import admin
from main.models import Worksheet, Entry
from import_export import resources
from import_export.widgets import TimeWidget
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class EntryResource(resources.ModelResource):

    name = Field(
        attribute='worksheet__user__first_name', 
        column_name='Name')
    date = Field(
        column_name='Day',
        attribute='worksheet__date',
        widget=TimeWidget(format='%A'))
    class Meta:
        model = Entry
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'date', 'store',
                  'operation', 'start_time', 'end_time')
        export_order = fields
        widgets = {
                'start_time': {'format': '%I:%M:%S %p'},
                'end_time': {'format': '%I:%M:%S %p'},
                }

    
class EntryAdmin(ImportExportActionModelAdmin):
    resource_class = EntryResource
    view_on_site = True
    list_display = ('get_name', 'get_date', 'store',
                    'operation', 'start_time', 'end_time')

    def get_name(self, obj):
        first_name = obj.worksheet.user.first_name
        last_name = obj.worksheet.user.last_name
        return (f"{first_name} {last_name}")

    def get_date(self, obj):
        return obj.worksheet.date

    get_name.admin_order_field = 'worksheet'
    get_name.short_description = 'Name'
    get_date.admin_order_field = 'worksheet'
    get_date.short_description = 'Date'


class WorksheetResource(resources.ModelResource):

    full_name = Field()
    class Meta:
        model = Worksheet
        skip_unchanged = True
        report_skipped = False
        fields = ('full_name', 'date')

    def dehydrate_full_name(self, worksheet):
        return '%s %s' % (worksheet.user.first_name, worksheet.user.last_name)


class WorksheetAdmin(ImportExportActionModelAdmin):
    resource_class = WorksheetResource
    list_display = ('name', 'date')


admin.site.register(Worksheet, WorksheetAdmin)
admin.site.register(Entry, EntryAdmin)
