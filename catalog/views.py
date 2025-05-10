from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, Contact


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    # print(Product.objects.all().order_by('created_at')[:5])
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(
            f"Спасибо за обращение, {name}! Ваше сообщение получено! "
            f"Мы свяжемся с Вами по номеру {phone} в течение трех рабочий дней!")

    contact = Contact.objects.all()
    context = {'contacts': contact}
    return render(request, 'contacts.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)
