# Generated by Django 4.2 on 2025-02-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_users_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="profile_url",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
