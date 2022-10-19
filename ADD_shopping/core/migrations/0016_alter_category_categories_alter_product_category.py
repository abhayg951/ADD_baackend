# Generated by Django 4.1.2 on 2022-10-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_remove_product_slug_alter_category_categories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="categories",
            field=models.CharField(
                choices=[
                    ("WW", "Winter Wear"),
                    ("SW", "Summer Wear"),
                    ("TW", "Top wear"),
                    ("BW", "Bottom Wear"),
                    ("FW", "Foot wear"),
                    ("N", "Null"),
                ],
                max_length=2,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("WW", "Winter Wear"),
                    ("SW", "Summer Wear"),
                    ("TW", "Top wear"),
                    ("BW", "Bottom Wear"),
                    ("FW", "Foot wear"),
                    ("N", "Null"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]