from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview', 'created_at', 'is_published', 'count_of_views')
    search_fields = ('title', 'content')
    list_filter = ('title',)

