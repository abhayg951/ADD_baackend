# Generated by Django 4.1.2 on 2022-10-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_rename_discounted_mrp_product_discounted_percent"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(null=True),
        ),
    ]
