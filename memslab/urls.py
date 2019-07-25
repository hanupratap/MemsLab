from django.conf.urls import url, include
from memslab import views
from django.contrib.auth import views as auth_views

app_name = 'memslab'

urlpatterns = [

    url(r'^profile/$', views.profile, name="profile"),
    url(r'^Contact/$', views.About, name="about"),
    url(r'^detail/$', views.detail, name="detail"),    
    url(r'^detail/(?P<username>[\w\-]+)/$', views.show_profile, name="show_profile"),
    url(r'^projects/(?P<project_id>[\d\-]+)/$', views.show_projects, name="show_projects"),
    url(r'^projects$', views.IndexView, name='index'),
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name="register"),
    url(r'^register/faculty$', views.register_faculty, name="register_faculty"),
    url(r'^register/student$', views.register_student, name="register_student"),
    url(r'^profile/edit/(?P<emp_id>[\d\-]+)/$', views.main_form, name="form"),
    url(r'^profile/edit/detail/(?P<emp_id>[\d\-]+)/$', views.category_form, name="detail_form"),
    url(r'^projects/edit/(?P<proj_id>[\d\-]+)/$', views.manage_project, name="manage_projects"),
    url(r'^projects/edit/specs/$', views.project_specs, name="project_specs"),
    url(r'^profile/category/(?P<username>[\w\-]+)/(?P<top_id>[\d\-]+)/$', views.prof_cat, name="category"),
    url(r'^profile/edit/password/$', views.change_password, name="password"),
    url(r'^about/$', views.About, name="about"),
    url(r'^manage_projects/$', views.add_delete_projects, name='add_delete_projects'),
    url(r'^add_projects/$', views.add_projects, name='add_projects'),
    url(r'^manage_project_images/(?P<proj_id>[\d\-]+)/$', views.manage_project_images, name='manage_project_images'),
    url(r'^news/$', views.news, name="news"),
    url(r'^news/edit$', views.news_edit, name="news_edit"),
    url(r'^news/add$', views.news_add, name="news_add"),
    url(r'^news/(?P<news_id>[\d\-]+)/$', views.news_detail, name="news_detail"),
    url(r'^news/edit/(?P<news_id>[\d\-]+)/$', views.news_detail_edit, name="news_detail_edit"),  
    url(r'^area_of_research/$', views.area_of_research, name="area_of_research"),
    url(r'^area_of_research/edit$', views.area_of_research_edit, name="area_of_research_edit"),  
    url(r'^publications/$', views.publications, name="publications"),
    url(r'^publications/(?P<year>[\d\-]+)/$', views.publications_yrws, name="publications_yrws"),
    url(r'^publications/edit/$', views.edit_pubs, name="edit_pubs"), 

]   