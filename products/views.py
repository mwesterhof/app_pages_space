from django.http import HttpResponse
from django.views.generic import TemplateView


def testlist(request, **kwargs):
    return HttpResponse('test list')


def testdetail(request, **kwargs):
    return HttpResponse('test detail')


class TestTemplate(TemplateView):
    template_name = 'products/test.html'
