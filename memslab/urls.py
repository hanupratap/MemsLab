from django.conf.urls import url, include
from memslab import views
from django.contrib.auth import views as auth_views

app_name = 'memslab'

urlpatterns = [

    url(r'^profile/$', views.profile, name="profile"),
    url(r'^About/$', views.About, name="about"),
    url(r'^detail/$', views.detail, name="detail"),    
    url(r'^detail/(?P<username>[\w\-]+)/$', views.show_profile, name="show_profile"),
    url(r'^projects/(?P<project_id>[\d\-]+)/$', views.show_projects, name="show_projects"),
    url(r'memslab/$', views.IndexView, name='index'),
    url(r'^Accounts/login/$', auth_views.LoginView.as_view(template_name='memslab/login.html'), name="login"),
    url(r'^Accounts/logout/$', auth_views.LogoutView.as_view(template_name='memslab/logout.html'), name="logout"),  
    url(r'^register/$', views.register, name="register"),
    url(r'^profile/category/(?P<username>[\w\-]+)/(?P<top>[\w\-]+)/$', views.prof_cat, name="category"),
    url(r'^watchman/', include('watchman.urls')),
]   