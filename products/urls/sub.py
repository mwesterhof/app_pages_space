from django.http import HttpResponse
from django.urls import path


def fancy(request):
    return HttpResponse('found it (parent_page: {})'.format(request.parent_page))

urlpatterns = [
    path('some_fancy_thing/', fancy, name='sub_url'),
]
