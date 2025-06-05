from django.shortcuts import render

from .forms import ArticleForm
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ArticleCreateView(CreateView):
    """blog/article_create"""
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article_list')


class ArticleListView(ListView):
    """blog/article_list"""
    model = Article

    def get_queryset(self):
        """ Показывать только опубликованные статьи: is_published=True"""
        return Article.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
    """blog/article_detail"""
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()

        return self.object


class ArticleUpdateView(UpdateView):
    """blog/article_update"""
    model = Article
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:article_detail')

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('blog:article_detail', kwargs={'pk': pk})


class ArticleDeleteView(DeleteView):
    """blog/article_delete"""
    model = Article
    success_url = reverse_lazy('blog:article_list')
