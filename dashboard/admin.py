from django.contrib import admin
from .models import *
from django.http import HttpResponse
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                  for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected as CSV"


class ActionAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['action', 'code', 'created_at']
    actions = ["export_as_csv"]


class DeviceAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['device_name', 'phone', 'created_at']
    actions = ["export_as_csv"]


admin.site.register(Action, ActionAdmin)
admin.site.register(Device, DeviceAdmin)
