from django.conf.urls.defaults import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ella.core.urls')),
) + staticfiles_urlpatterns()
