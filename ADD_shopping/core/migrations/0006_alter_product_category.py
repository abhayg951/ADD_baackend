# Generated by Django 4.1.2 on 2022-10-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_rename_category_category_categories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("S", "Shirt"),
                    ("WW", "Winter Wear"),
                    ("TP", "Top wear"),
                    ("BP", "Bottom wear"),
                    ("FW", "Foot wear"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]
