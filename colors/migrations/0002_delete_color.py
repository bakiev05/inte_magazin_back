# Generated by Django 4.0.1 on 2022-01-10 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_color_color'),
        ('colors', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Color',
        ),
    ]
