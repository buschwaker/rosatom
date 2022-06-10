from django.conf.urls import url

from . import views

app_name = 'jobs'

urlpatterns = [
    url(r'^employee_update/(?P<employee_id>\d+)/$', views.employee_edit, name='employee_update'),
    url(r'^employee_create/', views.create_employee, name='employee_create'),
    url(r'^index/', views.index, name='index'),
]
