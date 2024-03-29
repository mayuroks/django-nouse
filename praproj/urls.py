from django.conf.urls import patterns, include, url
from newapp import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'newapp.views.index', name='index'),
    # url(r'^praproj/', include('praproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^post/(?P<post_id>\d+)/detail_html$', newapp.views.post_detail, name='post_detail'),

)
