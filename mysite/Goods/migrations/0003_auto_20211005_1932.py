# Generated by Django 3.2.7 on 2021-10-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_broadcategories_categories_goods_status_subcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcategories',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]