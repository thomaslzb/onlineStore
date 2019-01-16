# Generated by Django 2.0 on 2019-01-09 20:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='goods',
            field=models.ForeignKey(on_delete=True, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=True, related_name='goods', to='trade.OrderInfo', verbose_name='订单信息'),
        ),
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together={('user', 'goods')},
        ),
    ]
