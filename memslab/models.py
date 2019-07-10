import os

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from ckeditor_uploader.fields import RichTextUploadingField

class Departments(models.Model):
    dep = models.CharField(max_length=100, default='', blank=True)
    class Meta:
        verbose_name_plural = "Departmennts"
    def __str__(self):
        return '%s' % (self.dep)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_no = models.CharField(max_length=50, blank=True)
    emp_pic = models.ImageField(upload_to='profile_image', \
        blank=True, default='profile_image/default_img.png')
    researcher = models.BooleanField(default=False, null=True)
    coordinator = models.BooleanField(default=False, null=True)
    designation = models.CharField(max_length=20, null=True)
    education_short = models.CharField(max_length=500, null=True)
    department = models.ForeignKey(Departments, \
        on_delete=models.DO_NOTHING, null=True, blank=True)
    short_description = RichTextUploadingField(default='', blank=True)
    area_of_interest = models.TextField(blank=True)
    Chamber_Consultation_Hours = models.CharField(max_length=200, default='yet to announce')
    experience_in_years = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    skype_link = models.URLField(blank=True)
    website_link =  models.URLField(blank=True)
    class Meta:
        verbose_name_plural = "Employees"

    def __str__(self):
        return '%s ' % (self.user.first_name + ' '+  self.user.last_name) 

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Employee.objects.create(user=instance)
    post_save.connect(create_user_profile, sender=User)

class Project_type(models.Model):
    name = models.CharField(max_length=500, default='')
    class Meta:
        verbose_name_plural = "Project Specialization"
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=500, default='')
    specializaiton = models.ForeignKey(Project_type, \
        on_delete=models.DO_NOTHING, null=True, blank=True)
    description = RichTextUploadingField(default='', blank=True)
    short_description = models.TextField(default='')
    project_pic = models.ImageField(upload_to='project_image', blank=True)
    STATUS = ((0, 'Ongoing'), (1, 'Completed'))
    status = models.PositiveSmallIntegerField(choices=STATUS, default=0)
    budget = models.CharField(max_length=200, default=None, blank=True)
    def __str__(self):
        return self.name
    people = models.ManyToManyField(Employee)
    sponsoring_agency = models.CharField(max_length=200, default='')
    proj_file = models.FileField(upload_to='project_files', null=True, blank=True) 
    def filename(self):
        return os.path.basename(self.proj_file.name)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Employee(user=user)
        user_profile.save()
    post_save.connect(create_profile, sender=user)

class project_image(models.Model):
    project = models.ForeignKey(Project ,on_delete=models.DO_NOTHING, \
        blank=True, null=True)
    pic = models.ImageField(upload_to='project_image', blank=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=400, default='', \
        blank=True, null=True)
    class Meta:
        verbose_name_plural = "Images for Projects"
    def __str__(self):
        return self.project.name

class Employee_details_topic(models.Model):
    topic = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Topic for Employee Details"



class Employeedetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True)
    topic = models.ForeignKey(Employee_details_topic, \
        on_delete=models.DO_NOTHING, blank=False, null=True)
    entry = RichTextUploadingField(default='', blank=True)
    def get_entry(self):
        return self.entry.split('\n')
    class Meta:
        verbose_name_plural = "Employee Details"
    def __str__(self):
        return self.user.first_name

class News(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE,blank=True, null=True)
    topic = models.CharField(max_length=300, blank=True)
    entry = RichTextUploadingField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    pic = models.ImageField(upload_to='project_image', blank=True)
    summary = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = "News"
    def __str__(self):
        return self.topic

