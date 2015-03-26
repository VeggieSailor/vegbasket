from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vegbasketapp.views.home', name='home'),
    url(r'^$', 'vegbasketapp.home.views.index', name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),



    url(r'^transformer/entry/(?P<entry_id>.*)/map$', 'vegbasketapp.transformer.views.entry_map', name='map'),


)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

