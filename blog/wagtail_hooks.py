from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Article


class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'author')
    list_filter =('author',)
    menu_icon = 'fa-file'
    menu_label = 'blog articles'
    model = Article

modeladmin_register(ArticleAdmin)
