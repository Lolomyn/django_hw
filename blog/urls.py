from django.urls import path, include
from blog.apps import BlogConfig
from . import views

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/article_list/', views.ArticleListView.as_view(), name='article_list'),
    path('blogs/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('blogs/create', views.ArticleCreateView.as_view(), name='article_create'),
    path('blogs/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('blogs/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
]
