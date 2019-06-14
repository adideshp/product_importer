import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'sku': ['icontains', ],
            'name': ['icontains', ],
            'status': ['exact']
        }