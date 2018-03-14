from django.http import HttpResponse
from django.views.generic import TemplateView


def testlist(request, **kwargs):
    return HttpResponse('test list')


def testdetail(request, **kwargs):
    return HttpResponse('test detail')


class TestTemplate(TemplateView):
    template_name = 'products/test.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'kwarg_based': kwargs['parent_page'],
            'self_based': self.parent_page
        })
        return ctx
