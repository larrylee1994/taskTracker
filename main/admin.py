from django.contrib import admin
from main.models import Worksheet, Entry
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


# TODO Set up admin export panel

admin.site.register(Worksheet)


class EntryResource(resources.ModelResource):

    # myfield = Field(column_name='myfield')
    # full_title = Field()
    class Meta:
        model = Entry
        skip_unchanged = True
        report_skipped = False
        fields = ('worksheet__name', 'worksheet__date', 'store',
                  'operation', 'start_time', 'end_time')
        export_order = fields

    # def dehydrate_full_title(self, entry):
    #     return '%s in %s' % (entry.operation, entry.store)


# class ExpiryDateFilter(admin.SimpleListFilter):

#     title = ('Date')

#     parameter_name = 'date'

#     def lookups(self, request, model_admin):
#        """
#            List of values to allow admin to select
#        """
#        return (
#           ('valid', ('All Valid')),
#           ('invalid', ('All Invalid')),
#        )

#     def queryset(self, request, queryset):
#         """
#             Return the filtered queryset
#         """

#         if self.value() == 'valid':
#             return queryset.filter(date__gt=datatime.datatime.now())
#         elif self.value() == 'invalid':
#             return queryset.filter(date__lt=datatime.datatime.now())
#         else:
#             return queryset

# class youModelAdminClass(admin.ModelAdmin):

#     list_filter = [ExpiryDateFilter]
#     list_display = ['DateValidity']
class EntryAdmin(ImportExportModelAdmin):
    resource_class = EntryResource

admin.site.register(Entry, EntryAdmin)
