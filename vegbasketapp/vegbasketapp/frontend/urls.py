from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    url(r'^$', 'vegbasketapp.frontend.views.index', name='frontend'),
    url(r'^entry_example/$', 'vegbasketapp.frontend.views.entry_example', name='entry_example'),
    

    
)

