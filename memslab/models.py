from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save





class Project_type(models.Model):
    name = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.name


class Project(models.Model):
    specializaiton = models.ForeignKey(Project_type, \
        on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=500, default='')
    description = models.CharField(max_length=4000, default='')
    project_pic = models.ImageField(upload_to='project_image', blank=True)
    STATUS = ((0, 'Ongoing'), (1, 'Completed'))
    status = models.PositiveSmallIntegerField(choices=STATUS, default=0)
    Person1 = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        related_name="first_proj", null=True, blank=True)
    Person2 = models.ForeignKey(User, on_delete=models.DO_NOTHING,\
         related_name="second_proj", null=True, blank=True)
    Person3 = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        related_name="third_proj", null=True, blank=True)
    Person4 = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        related_name="forth_proj", null=True, blank=True)
    Person5 = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        related_name="fifth_proj", null=True, blank=True)
    budget = models.CharField(max_length=200, default=None, blank=True)
    def __str__(self):
        return self.name


class Departments(models.Model):
    dep = models.CharField(max_length=100, default='')
    class Meta:
        verbose_name_plural = "Departmennts"
    def __str__(self):
        return '%s' % (self.dep)



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE", null=True)
    id_no = models.CharField(max_length=50, default='')
    emp_pic = models.ImageField(upload_to='profile_image', \
        blank=True, default='profile_image/default_img.png')
    researcher = models.BooleanField(default=False)
    coordinator = models.BooleanField(default=False)
    designation = models.CharField(max_length=20, null=True)
    department = models.ForeignKey(Departments, \
        on_delete=models.DO_NOTHING, null=True, blank=True)
    short_description = models.TextField(max_length=400, default='', blank=True, null=True)
    area = models.TextField(blank=True)
    Chamber_Consultation_Hours = models.CharField(max_length=200, default='yet to announce')
    #Employee working on project
    
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    def __str__(self):
        return '%s' % (self.user)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Employee(user=user)
        user_profile.save()
    post_save.connect(create_profile, sender=user)

class Employee_details_topic(models.Model):
    topic = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Topic for Employee Details"



class Employee_details(models.Model):
    user = models.ForeignKey(User, on_delete="models.DO_NOTHING", \
        blank=True, null=True)
    topic = models.ForeignKey(Employee_details_topic, \
        on_delete=models.DO_NOTHING, blank=False, null=True)
    sub_topic = models.CharField(max_length=500, default='')
    entry = models.TextField(default='')
    class Meta:
        verbose_name_plural = "Employee Details"
    def __str__(self):
        return self.user.first_name

class project_image(models.Model):
    project = models.ForeignKey(Project ,on_delete="models.DO_NOTHING", \
        blank=True, null=True)
    pic = models.ImageField(upload_to='project_image', blank=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=400, default='', \
        blank=True, null=True)

    def __str__(self):
        return self.project.name
