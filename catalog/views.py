from .forms import ProductForm, ProductModeratorForm
from django.core.exceptions import PermissionDenied
from .models import Product, Category, Contact
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        """ Показывать только опубликованные статьи: is_published=Published"""
        return Product.objects.filter(is_published='published')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return ProductForm
        if user.has_perm('catalog.can_unpublished_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsCreateView(CreateView):
    model = Contact
    fields = ['name', 'phone', 'message']
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()

        return context
