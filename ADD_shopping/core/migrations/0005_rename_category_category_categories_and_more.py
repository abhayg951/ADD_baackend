# Generated by Django 4.1.2 on 2022-10-18 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_categories_category_category_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="category",
            new_name="categories",
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="core.category",
            ),
        ),
    ]
