# Generated by Django 3.2.5 on 2021-07-15 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='quantity',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_alert',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='sku',
        ),
    ]