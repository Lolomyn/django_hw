from django import forms
from .models import Product
from PIL import Image
import sys


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_published',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['created_at', 'updated_at', 'owner']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        STOP_WORDS = ["казино", "биржа", "обман", "криптовалюта", "дешево", "полиция", "крипта", "бесплатно", "радар"]

        if name and description:
            for word in STOP_WORDS:
                if word in name.lower():
                    self.add_error('name', 'Эти слова запрещено использовать.')
                    break
                if word in description.lower():
                    self.add_error('description', 'Эти слова запрещено использовать.')
                    break

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            self.add_error('price', "Цена не может быть отрицательной")

        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            allowed_extensions = ['.jpg', '.jpeg', '.png']
            if not any(str(image).lower().endswith(ext) for ext in allowed_extensions):
                self.add_error('image', 'Загрузите изображение формата JPEG или PNG')

            if image.size > 5 * 1024 * 1024:
                self.add_error('image', "Максимальный вес загружаемого изображения 5 МБ")

        return image
