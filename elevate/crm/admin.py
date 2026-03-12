from django.contrib import admin
from .models import Employee

from import_export.admin import ImportExportModelAdmin

admin.site.register(Employee,ImportExportModelAdmin)