# Generated by Django 2.0 on 2019-01-10 15:45

import DUEditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190110_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_desc',
            field=DUEditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]
