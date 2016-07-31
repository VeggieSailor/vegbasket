from django.conf.urls import patterns, include, url
import django.views.static
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from datetime import date
from meta.views import Meta
from haystack.generic_views import SearchView
from django.conf.urls.i18n import i18n_patterns

import vegbasketapp.home.views
import vegbasketapp.frontend.views
import vegbasketapp.vegapi.views
import vegbasketapp.transformer.views
import vegbasketapp.personal.views
import vegbasketapp.recipe.views
import vegbasketapp.diary.views
#from registration.views import RegistrationView
from registration.backends.hmac.views import RegistrationView


#from vegbasketapp.frontend.models import RecaptchaRegistrationForm

from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import ReCaptchaField

class RecaptchaRegistrationForm(RegistrationFormUniqueEmail):
    recaptcha = ReCaptchaField(label="I'm a human")
    
    
class MySearchView(SearchView):
    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset.order_by('-photos', '-level', '-rating')

    
urlpatterns = [
    
    url(r'^visit/(?P<entry_id>\d*)/$', vegbasketapp.diary.views.visit, name='visit'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'accounts/register/$', RegistrationView.as_view(form_class=RecaptchaRegistrationForm),name='registration_register',),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'recipes/vegan-french-pate/$', vegbasketapp.recipe.views.recipe_french_pate),
    url(r'recipes/mediterranean-tabbouleh-salad/$', vegbasketapp.recipe.views.mediterranean_tabbouleh_salad),
    
    url(r'^i18n/', include('django.conf.urls.i18n')),
                       
    url(r'^$', vegbasketapp.home.views.index, name='home'),
    url(r'^map/$', vegbasketapp.frontend.views.homepage_map, name='home'),
    url(r'^vegapi/closest$', vegbasketapp.vegapi.views.get_closest, name='vegapi_get_closest'),
    url(r'^vegapi/box$', vegbasketapp.vegapi.views.get_box, name='vegapi_get_box'),
    
    url(r'opensource$', vegbasketapp.home.views.opensource, name='opensource'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^e404$', vegbasketapp.home.views.handler404),
    url(r'^e500$', vegbasketapp.home.views.handler500),
    url(r'^transformer/entry/(?P<entry_id>\d*)/reviews$', vegbasketapp.transformer.views.entry_reviews, name='reviews'),
    url(r'^transformer/entry/(?P<entry_id>\d*)/map$', vegbasketapp.transformer.views.entry_map, name='map'),
    url(r'^transformer/entry/(?P<entry_id>.*)$', vegbasketapp.transformer.views.entry, name='entry'),
    url(r'^transformer/region/(?P<region_id>.*)$', vegbasketapp.transformer.views.region, name='region'),
    url(r'^transformer/region$', vegbasketapp.transformer.views.region_root, name='region_root'),
    url('', include('social.apps.django_app.urls', namespace='social')),    
    url(r'^accounts/setup/$', vegbasketapp.personal.views.accounts_setup, name='accounts_setup'),
    url(r'^p/$', vegbasketapp.personal.views.personal, name='personal'),
    url('^logout/', auth_views.logout_then_login, {'login_url':"/accounts/login/"}, name='logout'),
    #url(r'^search/', include('haystack.urls'))
    #url('^', include('django.contrib.auth.urls')),
    url(r'^.*', include('vegbasketapp.frontend.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^search/?$', MySearchView.as_view(), name='search_view'),

)

urlpatterns += [
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    ]

urlpatterns += i18n_patterns(
    url(r'^(?P<slug>[\w-]+)/$', vegbasketapp.frontend.views.entry_slug, name='entry_slug'),

)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

