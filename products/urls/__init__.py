from django.conf.urls import include, url

from ..views import testdetail, testlist

from . import sub_urls


urlpatterns = [
    url(r'^$', testlist, name='testlist'),
    url(r'^(?P<pk>[0-9]+)/', testdetail, name='testdetail'),
    url(r'sub/', include(sub_urls)),
]
