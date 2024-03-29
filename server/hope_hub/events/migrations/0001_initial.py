# Generated by Django 4.2.7 on 2024-01-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Engagement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("date", models.DateField()),
                ("relevant_location", models.TextField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("comp_equity", models.BooleanField(default=False, help_text="Interwoven Equity")),
                ("comp_community", models.BooleanField(default=False, help_text="Healthy Community")),
                ("comp_nature", models.BooleanField(default=False, help_text="Harmony with Nature")),
                ("comp_environment", models.BooleanField(default=False, help_text="Livable Built Environment")),
                ("conn_past", models.BooleanField(default=False, help_text="Processing the past")),
                ("conn_present", models.BooleanField(default=False, help_text="Understanding the present")),
                ("conn_future", models.BooleanField(default=False, help_text="Visioning the future")),
            ],
        ),
    ]
