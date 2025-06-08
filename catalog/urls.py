from django.urls import path, include
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/product_list', views.ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create', views.ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('catalog/contacts/', views.ContactsCreateView.as_view(), name='contacts'),
    path('catalog/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/category/<int:category_id>/', views.CategoryListView.as_view(), name='category_list')
]
