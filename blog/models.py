from django.contrib.auth import get_user_model
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page

from app_pages.models import AppPageMixin

User = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class BlogPage(AppPageMixin, Page):
    url_config = 'blog.urls'

    limit_for_author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('limit_for_author'),
    ]
