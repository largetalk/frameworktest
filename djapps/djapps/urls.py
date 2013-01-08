from django.conf.urls import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^bigrender$', 'foo.views.bigrender', name='bigrender'),
    url(r'^empty$', 'foo.views.empty_template', name='empty_template'),
    url(r'^trender$', 'foo.views.trender', name='trender'),
    url(r'^calc$', 'foo.views.calc', name='calc'),
    #url(r'^foo/', include('djapps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += patterns('',
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#    {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
#)
