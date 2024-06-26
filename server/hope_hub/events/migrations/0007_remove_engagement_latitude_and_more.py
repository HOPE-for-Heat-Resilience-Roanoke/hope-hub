# Generated by Django 4.2.7 on 2024-05-03 00:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0006_engagement_place_alter_artifact_alt_text_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="engagement",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="engagement",
            name="longitude",
        ),
        migrations.RemoveField(
            model_name="engagement",
            name="relevant_location",
        ),
        migrations.AlterField(
            model_name="engagement",
            name="comp_community",
            field=models.BooleanField(
                default=False, help_text="Healthy Community", verbose_name="Comp Plan Community"
            ),
        ),
        migrations.AlterField(
            model_name="engagement",
            name="comp_environment",
            field=models.BooleanField(
                default=False, help_text="Livable Built Environment", verbose_name="Comp Plan Environment"
            ),
        ),
        migrations.AlterField(
            model_name="engagement",
            name="comp_equity",
            field=models.BooleanField(default=False, help_text="Interwoven Equity", verbose_name="Comp Plan Equity"),
        ),
        migrations.AlterField(
            model_name="engagement",
            name="comp_nature",
            field=models.BooleanField(default=False, help_text="Harmony with Nature", verbose_name="Comp Plan Nature"),
        ),
        migrations.AlterField(
            model_name="engagement",
            name="conn_future",
            field=models.BooleanField(
                default=False, help_text="Visioning the Future", verbose_name="Connection Future"
            ),
        ),
        migrations.AlterField(
            model_name="engagement",
            name="conn_past",
            field=models.BooleanField(default=False, help_text="Processing the Past", verbose_name="Connection Past"),
        ),
        migrations.AlterField(
            model_name="engagement",
            name="conn_present",
            field=models.BooleanField(
                default=False, help_text="Understanding the Present", verbose_name="Connection Present"
            ),
        ),
    ]
