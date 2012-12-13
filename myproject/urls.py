import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^squash/$', 'squash.views.index'),
    (r'^squash/(?P<match_id>\d+)/$', 'squash.views.match'),
    (r'^squash/(?P<match_id>\d+)/edit/$', 'squash.views.edit_match'),
    (r'^squash/(?P<match_id>\d+)/add/$', 'squash.views.add_match'),
    (r'^squash/events/$', 'squash.views.event_list'),
    (r'^squash/events/add/$', 'squash.views.event_add'),
    #(r'^squash/events/(?P<event_id>\d+)/$', 'squash.views.event'),
    (r'^squash/login/$', 'squash.views.auth_login',),
    (r'^squash/logout/$', 'squash.views.auth_logout',),
    #(r'^squash/standings/$', 'polls.views.standings'),
    (r'^admin/', include(admin.site.urls)),
    
)