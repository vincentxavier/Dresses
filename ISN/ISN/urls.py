from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ISN.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dresses/', include('dresses.urls')),
    url(r'^HurryUp/', include('HurryUp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
