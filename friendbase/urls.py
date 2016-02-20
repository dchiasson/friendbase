from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'friendbase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/$', 'friendbase.polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'friendbase.polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'friendbase.polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'friendbase.polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
