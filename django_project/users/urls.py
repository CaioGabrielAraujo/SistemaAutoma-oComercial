from django.conf.urls import url

from . import views
app_name = 'users'
urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^login/$', views.show_login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^self_edit/', views.self_edit_user, name="self_edit_user"),
    url(r'^register/', views.register, name="register"),
    url(r'^list_user_edit/', views.list_user_edit, name="listuseredit"),
    url(r'^list_user/', views.list_user, name="listuser"),
    url(r'^edit_user/(?P<user_id>[0-9]+)/', views.edit_user, name="edit_user"),
]
