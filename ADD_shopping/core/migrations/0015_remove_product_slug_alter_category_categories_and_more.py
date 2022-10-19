# Generated by Django 4.1.2 on 2022-10-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="slug",
        ),
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
                    ("N", "NUll"),
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
                    ("N", "NUll"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]