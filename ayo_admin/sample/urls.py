from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api

from api import SampleResource, UserResource
sample_resource = SampleResource()

v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(SampleResource())

urlpatterns = patterns('sample.views',
    url(r'^$', 'index', name="sample-index"),
)

if settings.NEED_SUPPORT_RESTFUL_API:
    urlpatterns += patterns('',
        url(r'^api/', include(v1_api.urls)),
)
