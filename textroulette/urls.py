from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

from textroulette.apps.main.views import Home, Success, Duplicate, Twilio


urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name="home"),
    url(r'^success/$', Success.as_view(), name="success"),
    url(r'^duplicate/$', Duplicate.as_view(), name="duplicate"),
    url(r'^twilio/$', Twilio.as_view(), name="twilio"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Static-y pages
    #url(r'^about/$', About.as_view(), name="about"),
    #url(r'^contact/$', Contact.as_view(), name='contact'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        )
