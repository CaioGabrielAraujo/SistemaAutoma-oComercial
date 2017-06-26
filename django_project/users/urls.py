from django.conf.urls import url

from . import views
app_name = 'users'
urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^login/$', views.show_login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^self_edit/', views.self_edit_user, name="self_edit_user"),
     url(r'^register/', views.register, name="register"),
]
