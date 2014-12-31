from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^rest/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^interview/', include('web.urls')),
)
