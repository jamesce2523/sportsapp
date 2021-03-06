from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'basketball.views.home', name='home'),
    url(r'^team/(?P<pk>\d+)$', 'basketball.views.team', name='team'),
    url(r'^player/(?P<pk>\d+)$', 'basketball.views.player', name='player'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
