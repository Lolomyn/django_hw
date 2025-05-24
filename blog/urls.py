from django.urls import path, include
from blog.apps import BlogConfig
from . import views

app_name = BlogConfig.name

urlpatterns = [
    path('blog/article_list/', views.ArticleListView.as_view(), name='article_list'),
    path('blog/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('blog/create', views.ArticleCreateView.as_view(), name='article_create'),
    path('blog/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('blog/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
]
