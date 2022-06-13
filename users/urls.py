from django.contrib.auth.views import logout
from django.conf.urls import url

from .views import my_login, signup_view


app_name = 'users'

urlpatterns = [
    url(
        'logout/',
        logout,
        name='logout'
    ),
    url(
        'login/',
        my_login,
        {'template_name': 'users/login.html'},
        name='login',
    ),
    url('signup/', signup_view, name='sign-up'),
]
