from django.contrib import admin
from .models import Commission, Job, JobApplication


class JobInline(admin.StackedInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInline]

    search_fields = ['title']
    list_display = ['title', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']


class JobAdmin(admin.ModelAdmin):
    model = Job


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)