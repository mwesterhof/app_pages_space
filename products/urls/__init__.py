from django.conf.urls import url
from django.urls import include, path

from ..views import ProductList, ProductDetail

from . import sub


urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path(r'sub/', include(sub)),
]
