# Generated by Django 4.1.2 on 2022-10-19 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_alter_category_categories_alter_product_category"),
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
                max_length=10,
                null=True,
            ),
        ),
    ]
