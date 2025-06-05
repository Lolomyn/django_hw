from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    is_published = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft',
                                    verbose_name='Статус публикации')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', verbose_name='Владелец')

    def __str__(self):
        return f"{self.name}, {self.price} руб. Товар из категории {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['name']
        permissions = [
            ('can_unpublished_product', 'Can unpublished product')
        ]


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя', null=True, blank=False)
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True, blank=False)
    message = models.TextField(verbose_name='Сообщение', null=True, blank=False)

    def __str__(self):
        return f"{self.name} - {self.phone}. {self.message}"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
        ordering = ["name"]
