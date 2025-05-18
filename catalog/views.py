from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, Contact
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ContactsCreateView(CreateView):
    model = Contact
    fields = ['name', 'phone', 'message']
    template_name = 'contacts.html'
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()

        return context

# def home(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     # print(Product.objects.all().order_by('created_at')[:5])
#     return render(request, 'home.html', context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         return HttpResponse(
#             f"Спасибо за обращение, {name}! Ваше сообщение получено! "
#             f"Мы свяжемся с Вами по номеру {phone} в течение трех рабочий дней!")
#
#     contact = Contact.objects.all()
#     context = {'contacts': contact}
#     return render(request, 'contacts.html', context)


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product
#     }
#
#     return render(request, 'product_detail.html', context)
