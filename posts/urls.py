from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('carlsblog.posts.views',
    url(r'^$', 'post_list'),
    url(r'^(?P<post_id>\d+)/$', 'post_detail'),
)
