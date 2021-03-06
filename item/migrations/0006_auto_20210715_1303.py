# Generated by Django 3.2.5 on 2021-07-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20210715_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='product_alert',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=225),
        ),
    ]
