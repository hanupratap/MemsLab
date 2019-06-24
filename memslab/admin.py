from django.contrib import admin
from memslab.models import Employee,Project,Employeedetails,Employee_details_topic,Departments,project_image,Project_type
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'MEMS Admin'

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('user','designation','researcher','id_no')
    list_filter=('researcher',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project)
admin.site.register(Employeedetails)
admin.site.register(Employee_details_topic)
admin.site.register(Departments)
admin.site.register(project_image)
admin.site.register(Project_type)
admin.site.unregister(Group)


admin.site.site_url = "/memslab"