# Generated by Django 4.0 on 2022-12-15 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0015_alter_productcategory_categoryname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
