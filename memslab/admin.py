from django.contrib import admin
from memslab.models import *
from django.contrib.auth.models import Group
from django import forms
# Register your models here.
admin.site.site_header = 'MEMSLab '

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('user','designation','researcher','id_no')
    list_filter=('researcher',)

class emp_details_subtopic(admin.TabularInline):
    model = Employeedetails

class Emp_details_topics(admin.ModelAdmin):
    inlines = [emp_details_subtopic]
    class Meta:
        model = Employee_details_topic

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project)
admin.site.register(Employeedetails)
admin.site.register(Employee_details_topic, Emp_details_topics)
admin.site.register(Departments)
admin.site.register(project_image)
admin.site.register(Project_type)
admin.site.register(News)
admin.site.register(Publications)
admin.site.register(Area_of_research)