from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filters import GoodsFilters
from .models import Goods, GoodsCategory, HotSearchWords, Banner
from .serializers import GoodsSerializer, CategorySerializer, HotSearchSerializer
from .serializers import BannersSerializer, IndexCategorySerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    Goods List , Pagination, Search, Filter, Ordering
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilters
    ordering_fields = ('sold_num', 'shop_price')
    search_fields = ('name', 'goods_desc')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    List:
        Goods Category List
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchWordsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    List:
        Hot Search Words List
    """
    queryset = HotSearchWords.objects.all().order_by('index')
    serializer_class = HotSearchSerializer


class BannersViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    List:
        Goods Banners List
    """
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannersSerializer


class IndexCategoryViewset(mixins.ListModelMixin, GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer
