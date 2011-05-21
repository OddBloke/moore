from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('matches.views',
    url(r'^$','index'),
    url(r'^details/(?P<match_id>\d+)/$','match_details'),
)

