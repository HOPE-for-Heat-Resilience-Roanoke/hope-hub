# Generated by Django 4.2.7 on 2024-06-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0015_alter_engagement_conn_future_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="downloadablefile",
            name="is_audio",
            field=models.BooleanField(
                default=False,
                help_text="If checked, this file will appear with an audio player on the hub.",
                verbose_name="Audio",
            ),
        ),
    ]
