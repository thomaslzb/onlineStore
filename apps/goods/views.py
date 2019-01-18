from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import GoodsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Goods
from .filters import GoodsFilters


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Goods List , Pagination, Search, Filter, Ordering
    """
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilters
    ordering_fields = ('goods_num', 'add_time')
    search_fields = ('name', 'goods_desc')
