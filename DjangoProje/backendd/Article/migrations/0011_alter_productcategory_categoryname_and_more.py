# Generated by Django 4.0 on 2022-12-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0010_product_in_stock_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='categoryName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
