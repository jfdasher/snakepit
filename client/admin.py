from django.contrib import admin

# Register your models here.

from .models import *
from django.forms import TextInput, Textarea
from django.db import models
#from tinymce.widgets import TinyMCE

class ReportCompanyInline(admin.TabularInline):
    model = ReportCompany
    extra = 1

class ReportReportInline(admin.TabularInline):
    model = ReportReport
    fk_name = 'parent'
    extra = 1

class ReportFileInline(admin.TabularInline):
    model = ReportFile
    extra = 1




class ReportModelAdmin(admin.ModelAdmin):
    inlines = (ReportCompanyInline,ReportReportInline,)
    list_display = ('title', 'release_date', 'status', 'product_line', 'rendering_strategy')

#    formfield_overrides = {
#        #models.TextField: {'widget':TinyMCE(attrs={'cols': 80, 'rows': 30})},
#    }
admin.site.register(Report, ReportModelAdmin)


#admin.site.register(Report)

admin.site.register(ReportStatus)
admin.site.register(ReportType)
admin.site.register(ReportRenderingStrategy)
admin.site.register(ReportRelationshipType)
admin.site.register(Company)
admin.site.register(ProductLine)

admin.site.register(ReportCompany)
admin.site.register(ReportReport)
admin.site.register(ReportFileType)
