from django.views.generic import CreateView, DetailView, ListView

from .forms import CreateArticleForm
from .models import Article


class FilteredArticleMixin:
    model = Article

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.parent_page.limit_for_author:
            return qs.filter(author = self.parent_page.limit_for_author)
        return qs


class ArticleList(FilteredArticleMixin, ListView):
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['parent_page'] = self.parent_page
        return ctx


class ArticleDetail(FilteredArticleMixin, DetailView):
    pass


class CreateArticleView(CreateView):
    model = Article
    form_class = CreateArticleForm

    def get_success_url(self):
        return self.parent_page.reverse('article_detail', pk=self.object.pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
