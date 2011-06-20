from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('carlsblog.posts.views',
    url(r'^$', 'index'),
    url(r'^(?P<post_id>\d+)/$', 'show_post'),
)
