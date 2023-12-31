# Generated by Django 4.2.4 on 2023-09-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("activated", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254)),
                ("name", models.CharField(max_length=150)),
                ("profile_image", models.CharField(blank=True, null=True)),
                ("role", models.IntegerField(default=0)),
                ("uid", models.CharField(max_length=150)),
                ("anonymous", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "ユーザー",
                "verbose_name_plural": "ユーザー",
                "db_table": "users",
                "indexes": [
                    models.Index(condition=models.Q(("email__isnull", False)), fields=["email"], name="index_users_on_email"),
                    models.Index(condition=models.Q(("uid__isnull", False)), fields=["uid"], name="index_users_on_uid"),
                ],
            },
        ),
    ]
