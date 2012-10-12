from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# for RESTful APIs
from tastypie.api import Api
from account.api import AccountResource, UserResource, FollowRelationResource, ContactGroupResource
v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(AccountResource())
v1_api.register(FollowRelationResource())
v1_api.register(ContactGroupResource())

from venue.api import VenueResource
v1_api.register(VenueResource())

from shout.api import ShoutResource, ShoutCommentResource, ShoutReportResource
v1_api.register(ShoutResource())
v1_api.register(ShoutCommentResource())
v1_api.register(ShoutReportResource())

from notification.api import ShoutNotificationResource
v1_api.register(ShoutNotificationResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BB_Backend.views.home', name='home'),
    # url(r'^BB_Backend/', include('BB_Backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/account/login/$', "account.views.login", name="account-login"),
    url(r'^api/v1/account/register/$', "account.views.register", name="account-register"),
    url(r'^api/v1/account/facebook_connection/$', "account.views.facebook_connection", name="account-facebook-connection"),
    url(r'^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        )
