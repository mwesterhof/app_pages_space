from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page

from app_pages.models import AppPageMixin


THEMES = [
    ('dark', "Dark"),
    ('light', "Light"),
]


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductPage(AppPageMixin, Page):
    url_config = 'products.urls'

    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True)
    theme = models.CharField(
        choices=THEMES, max_length=10, default=THEMES[0][0])

    settings_panels = Page.settings_panels + [
        MultiFieldPanel(
            [
                FieldPanel('category'),
                FieldPanel('theme'),
            ],
            heading="Product app settings",
            classname="collapsible collapsed"
        )
    ]
