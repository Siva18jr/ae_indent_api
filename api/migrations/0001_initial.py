# Generated by Django 4.2 on 2024-10-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OutletProducts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_id", models.TextField(null=True)),
                ("shift", models.IntegerField()),
                ("image_url", models.CharField(max_length=255)),
                ("product_name", models.CharField(max_length=50)),
                ("product_price", models.CharField(max_length=50)),
                ("product_details", models.CharField(max_length=255)),
                ("product_category", models.CharField(max_length=50)),
                ("quantity", models.CharField(max_length=20, null=True)),
                ("date", models.CharField(max_length=50)),
                ("total_product_price", models.CharField(max_length=50, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Outlets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
                ("number", models.CharField(max_length=12)),
                ("storeId", models.CharField(max_length=20)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("price", models.CharField(max_length=50)),
                ("details", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="")),
                ("quantity", models.CharField(default=1, max_length=20, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="RemainingProducts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_id", models.TextField(null=True)),
                ("shift", models.IntegerField()),
                ("image_url", models.CharField(max_length=255)),
                ("product_name", models.CharField(max_length=50)),
                ("product_price", models.CharField(max_length=50)),
                ("product_details", models.CharField(max_length=255)),
                ("product_category", models.CharField(max_length=50)),
                ("date", models.CharField(max_length=50)),
                ("total_product_price", models.CharField(max_length=50, null=True)),
                ("quantity", models.CharField(max_length=20, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="SaleProducts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_details", models.TextField(null=True)),
                ("outlet_name", models.CharField(max_length=50)),
                ("outlet_location", models.CharField(max_length=50)),
                ("outlet_number", models.CharField(max_length=12)),
                ("outlet_store_id", models.CharField(max_length=20)),
                ("shift", models.IntegerField(null=True)),
                ("total", models.CharField(max_length=50, null=True)),
                ("cash", models.CharField(max_length=50, null=True)),
                ("date", models.CharField(max_length=50, null=True)),
                ("balance", models.CharField(max_length=50, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=70, null=True, unique=True
                    ),
                ),
                ("password", models.CharField(max_length=50)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
