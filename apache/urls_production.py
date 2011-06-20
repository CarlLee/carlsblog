from django.conf.urls.defaults import patterns, include, url
#import carlsblog.posts

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carlsblog.views.home', name='home'),
    # url(r'^carlsblog/', include('carlsblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', include('posts.urls'))
)
