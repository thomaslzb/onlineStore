import django_filters

from .models import Goods


class GoodsFilters(django_filters.rest_framework.FilterSet):
    """
    Goods filter Shop_price
    """
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    price_min = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    """
    icontains 前面的i表示忽视大小写
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        module = Goods
        fields = ['price_max', 'price_min', 'name']

