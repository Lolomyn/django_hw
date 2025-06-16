from .models import Product


class ProductService:
    @staticmethod
    def get_list_products_of_category(category_id):
        return Product.objects.filter(
            category_id=category_id,
            is_published='published'
        ).order_by('name')
