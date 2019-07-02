from django.conf.urls import url, include
from memslab import views
from django.contrib.auth import views as auth_views

app_name = 'memslab'

urlpatterns = [

    url(r'^memslab/profile/$', views.profile, name="profile"),
    url(r'^memslab/About/$', views.About, name="about"),
    url(r'^memslab/detail/$', views.detail, name="detail"),    
    url(r'^memslab/detail/(?P<username>[\w\-]+)/$', views.show_profile, name="show_profile"),
    url(r'^memslab/projects/(?P<project_id>[\d\-]+)/$', views.show_projects, name="show_projects"),
    url(r'memslab/$', views.IndexView, name='index'),
    url(r'^memslab/login/$', auth_views.LoginView.as_view(template_name='memslab/login.html'), name="login"),
    url(r'^memslab/logout/$', auth_views.LogoutView.as_view(template_name='memslab/logout.html'), name="logout"),  
    url(r'^memslab/register/$', views.register, name="register"),
    url(r'^memslab/profile/edit/(?P<emp_id>[\d\-]+)/$', views.main_form, name="form"),
    url(r'^memslab/profile/edit/detail/(?P<emp_id>[\d\-]+)/$', views.category_form, name="detail_form"),
    url(r'^memslab/profile/category/(?P<username>[\w\-]+)/(?P<top>[\w\-]+)/$', views.prof_cat, name="category"),
    url(r'^watchman/', include('watchman.urls')),
    url(r'^memslab/about/$', views.About, name="about"),
]   