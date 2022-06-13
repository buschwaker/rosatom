from django.conf.urls import url

from . import views

app_name = 'jobs'

urlpatterns = [
    url(r'^position_delete/(?P<position_id>\d+)/$', views.position_delete, name='position_delete'),
    url(r'^position_create/$', views.position_create, name='position_create'),
    url(r'^position_update/(?P<position_id>\d+)/$', views.position_edit, name='position_update'),
    url(r'^employee_delete/(?P<employee_id>\d+)/$', views.employee_delete, name='employee_delete'),
    url(r'^employee_update/(?P<employee_id>\d+)/$', views.employee_edit, name='employee_update'),
    url(r'^employee_create/$', views.create_employee, name='employee_create'),
    url(r'^$', views.index, name='index'),
]
