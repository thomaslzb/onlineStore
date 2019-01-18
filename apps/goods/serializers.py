from rest_framework import serializers

from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'name', 'shop_price', 'goods_brief', 'add_time']



