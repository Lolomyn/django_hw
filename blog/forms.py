from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ['created_at', 'is_published', 'count_of_views']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите заголовок статьи'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите текст статьи'
        })

        self.fields['preview'].widget.attrs.update({
            'class': 'form-control'
        })
