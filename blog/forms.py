from django import forms
from django.forms import widgets

from .models import Article


class CreateArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['author'].initial = user

    def clean_author(self):
        return self.user

    class Meta:
        model = Article
        fields = ['author', 'title', 'body']
