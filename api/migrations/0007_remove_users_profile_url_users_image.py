# Generated by Django 4.2 on 2025-02-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_users_profile_url"),
    ]

    operations = [
        migrations.RemoveField(model_name="users", name="profile_url",),
        migrations.AddField(
            model_name="users",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
