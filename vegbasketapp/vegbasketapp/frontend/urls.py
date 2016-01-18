from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    #url(r'^$', 'vegbasketapp.frontend.views.index', name='frontend'),
    url(r'^entry_example/$', 'vegbasketapp.frontend.views.entry_example', name='entry_example'),
    url(r'^e/vg/(?P<entry_id>.*)$', 'vegbasketapp.frontend.views.entry_vg', name='entry_vg'),
    url(r'^e/vs/(?P<entry_id>.*)$', 'vegbasketapp.frontend.views.entry_vs', name='entry_vs'),
    
    url(r'^(?P<slug>[\w-]+)/$', 'vegbasketapp.frontend.views.entry_slug', name='entry_slug'),
    
)
from django.conf.urls.i18n import i18n_patterns


