from django.views.generic import DetailView, ListView

from products.models import Product


class FilteredProductMixin:
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if not self.parent_page.category:
            return qs
        return qs.filter(category=self.parent_page.category)


class ProductList(FilteredProductMixin, ListView):
    pass


class ProductDetail(FilteredProductMixin, DetailView):
    pass
