from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from CS638_proj3.apps.main.views import Home


urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name="home"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Static-y pages
    #url(r'^about/$', About.as_view(), name="about"),
    #url(r'^contact/$', Contact.as_view(), name='contact'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
