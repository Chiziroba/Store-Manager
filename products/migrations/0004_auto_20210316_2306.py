# Generated by Django 3.1.7 on 2021-03-16 23:06

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210315_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='box_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.changeImageName),
        ),
    ]
