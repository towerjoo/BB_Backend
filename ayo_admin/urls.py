from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# for RESTful APIs
from tastypie.api import Api
from account.api import AccountResource, UserResource
v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(AccountResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ayo_admin.views.home', name='home'),
    # url(r'^ayo_admin/', include('ayo_admin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/account/login/$', "account.views.login", name="account-login"),
    url(r'^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        )
