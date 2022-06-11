from django.contrib.auth.views import login, logout
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
    url(
        'logout/',
        logout,
        name='logout'
    ),
    url(
        'login/',
        login,
        name='login'
    ),
]