from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('carlsblog.posts.views',
    url(r'^$', 'post_list'),
    url(r'^(?P<post_id>\d+)$', 'post_detail'),
    url(r'^publish$', 'post_publish'),
    url(r'^create$', 'post_create'),
)
