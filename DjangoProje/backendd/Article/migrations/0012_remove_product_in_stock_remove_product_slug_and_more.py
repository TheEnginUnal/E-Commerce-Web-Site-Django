# Generated by Django 4.0 on 2022-12-15 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0011_alter_productcategory_categoryname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='slug',
        ),
    ]