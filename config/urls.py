from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jobs/', include('jobs.urls', namespace='jobs')),
    url(r'^auth/', include('users.urls', namespace='users')),
    url(r'^auth/', include('django.contrib.auth.urls'))
]


if settings.DEBUG:

    import debug_toolbar

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)), ]
