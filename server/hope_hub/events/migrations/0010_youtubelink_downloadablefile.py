# Generated by Django 4.2.7 on 2024-05-13 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hope_hub.events.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0009_alter_engagement_place"),
    ]

    operations = [
        migrations.CreateModel(
            name="YoutubeLink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("link", models.URLField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
                ),
                ("engagement", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="events.engagement")),
            ],
        ),
        migrations.CreateModel(
            name="DownloadableFile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("upload", models.FileField(upload_to=hope_hub.events.models.engagement_date_path)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
                ),
                ("engagement", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="events.engagement")),
            ],
        ),
    ]