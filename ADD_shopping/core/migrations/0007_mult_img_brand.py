# Generated by Django 4.1.2 on 2022-10-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_rename_mrp_itemcard_original_mrp_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mult_img",
            name="brand",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
