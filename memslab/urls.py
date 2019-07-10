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
    url(r'^$', views.IndexView, name='index'),
    url(r'^login/$',  auth_views.LoginView.as_view(template_name='memslab/login.html'), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='memslab/logout.html'), name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^register/faculty$', views.register_faculty, name="register_faculty"),
    url(r'^register/student$', views.register_student, name="register_student"),
    url(r'^profile/edit/(?P<emp_id>[\d\-]+)/$', views.main_form, name="form"),
    url(r'^profile/edit/detail/(?P<emp_id>[\d\-]+)/$', views.category_form, name="detail_form"),
    url(r'^projects/edit/(?P<proj_id>[\d\-]+)/$', views.manage_project, name="manage_projects"),
    url(r'^profile/category/(?P<username>[\w\-]+)/(?P<top>[\w\-]+)/$', views.prof_cat, name="category"),
    url(r'^profile/edit/password/$', views.change_password, name="password"),
    url(r'^about/$', views.About, name="about"),
    url(r'^manage_projects/$', views.add_delete_projects, name='add_delete_projects'),
    url(r'^add_projects/$', views.add_projects, name='add_projects'),
    url(r'^manage_project_images/(?P<proj_id>[\d\-]+)/$', views.manage_project_images, name='manage_project_images'),
    url(r'^news/$', views.news, name="news"),
    url(r'^news/edit$', views.news_edit, name="news_edit"),
    url(r'^news/add$', views.news_add, name="news_add"),
    url(r'^news/(?P<news_id>[\d\-]+)/$', views.news_detail, name="news_detail"),
    url(r'^watchman/', include('watchman.urls')),
    url(r'^accounts/', include('allauth.urls')),
]   