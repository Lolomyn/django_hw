from django.urls import path, include
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.ProductListView.as_view(), name='home'),
    path('contacts/', views.ContactsCreateView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail')
]
