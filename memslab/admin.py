from django.contrib import admin
from memslab.models import Employee,Project,Employee_details,Employee_details_topic,Departments,project_image,Project_type


# Register your models here.


admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Employee_details)
admin.site.register(Employee_details_topic)
admin.site.register(Departments)
admin.site.register(project_image)
admin.site.register(Project_type)


admin.site.site_url = "/memslab"