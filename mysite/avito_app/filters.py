from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'subcategory': ['exact'],
            'price': ['gte', 'lte'],
            'article_name': ['exact'],
            'product_type': ['exact']
        }