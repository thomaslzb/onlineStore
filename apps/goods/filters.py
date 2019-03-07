import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFilters(django_filters.rest_framework.FilterSet):
    """
    Goods filter Shop_price
    """
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    price_min = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    """
    icontains 前面的i表示忽视大小写
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    """
    categories
    """
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        queryset = queryset.filter(Q(category__id=value) |
                                   Q(category__parent_category_id=value) |
                                   Q(category__parent_category__parent_category_id=value)
                                   )
        return queryset

    class Meta:
        module = Goods
        fields = ['price_max', 'price_min', 'name']

