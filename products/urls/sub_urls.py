from django.conf.urls import url

from ..views import testlist, TestTemplate


urlpatterns = [
    url(r'^$', testlist, name='testlist2'),
    url(r'^test/$', TestTemplate.as_view(), name='testtemplate')
]
