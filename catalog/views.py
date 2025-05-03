from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


def home(request):
    print(Product.objects.all().order_by('created_at')[:5])
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(
            f"Спасибо за обращение, {name}! Ваше сообщение получено! "
            f"Мы свяжемся с Вами по номеру {phone} в течение трех рабочий дней!")
    return render(request, 'contacts.html')
