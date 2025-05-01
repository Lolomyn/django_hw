from django.shortcuts import render
from django.http import HttpResponse


def home(request):
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

#
# def contact_form_feedback(request):
#
#     return render(request, 'contacts.html')
