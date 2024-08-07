from urllib.parse import urlparse, parse_qs

from django.conf import settings
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


class Place(models.Model):
    name = models.CharField(max_length=255)

    latitude = models.FloatField()
    longitude = models.FloatField()

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Engagement(models.Model):
    title = models.CharField(max_length=255, help_text="A name for your event/engagement/activity.")
    description = models.TextField(help_text="A short (2-3 sentence) explanation about what the event/engagement/activity was and its connection to heat resilience.")
    date = models.DateField(help_text="The date of the event/engagement/activity.")
    slug = AutoSlugField(populate_from="title", unique=True, null=True)

    place = models.ForeignKey(Place, on_delete=models.PROTECT, help_text="The relevant location for the event. Must be a specific place, not a region. Make sure to add the place before filling out this form.")

    comp_equity = models.BooleanField("Interwoven Equity", default=False, help_text="A theme from the City of Roanoke’s 2040 Comprehensive Plan")
    comp_community = models.BooleanField("Healthy Community", default=False, help_text="A theme from the City of Roanoke’s 2040 Comprehensive Plan")
    comp_nature = models.BooleanField("Harmony with Nature", default=False, help_text="A theme from the City of Roanoke’s 2040 Comprehensive Plan")
    comp_environment = models.BooleanField("Livable Built Environment", default=False, help_text="A theme from the City of Roanoke’s 2040 Comprehensive Plan")

    conn_past = models.BooleanField("Processing the Past", default=False, help_text="Does the engagement encourage reflection on the past?")
    conn_present = models.BooleanField("Understanding the Present", default=False, help_text="Does the engagement encourage reflection on the present?")
    conn_future = models.BooleanField("Visioning the Future", default=False, help_text="Does the engagement encourage reflection on the future?")

    approved = models.BooleanField("Ready for publishing on the hub", default=False, help_text="Visioning the Future")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date",)

    def to_json(self):
        return {
            "title": self.title,
            "slug": self.slug,
            "description": self.description,
            "date": self.date.isoformat(),
            "relevant_location": self.place.name,
            "latitude": self.place.latitude,
            "longitude": self.place.longitude,
            "comp_equity": self.comp_equity,
            "comp_community": self.comp_community,
            "comp_nature": self.comp_nature,
            "comp_environment": self.comp_environment,
            "conn_past": self.conn_past,
            "conn_present": self.conn_present,
            "conn_future": self.conn_future,
            "artifacts": [
                a.to_json() for a in self.artifact_set.all()
            ],
            "downloadablefiles": [
                d.to_json() for d in self.downloadablefile_set.all()
            ],
            "youtubelinks": [
                y.to_json() for y in self.youtubelink_set.all()
            ]
        }

    def get_absolute_url(self):
        return reverse(
            'events:detail', kwargs={"pk": self.pk}
        )

    def __str__(self):
        return f"{self.title} [{self.date.isoformat()}]"


def engagement_date_path(instance, filename):
    return "engagement_{}/{}/{}".format(
        instance.engagement.pk,
        instance.engagement.date.strftime("%Y/%m/%d"),
        filename
    )


class Artifact(models.Model):
    attribution = models.CharField("Attribution for Statement", max_length=255, blank=True, help_text="Will appear as the attribution for the connection to resilience statement (aka who said the statement).")
    statement = models.TextField("Connection to Community Resilience Statement", blank=True, help_text="Will appear as a block quote under the image.")
    engagement = models.ForeignKey(Engagement, on_delete=models.PROTECT)
    alt_text = models.CharField("Image Caption", max_length=255, help_text="Caption for the image, also used as the alt text.")
    upload = models.FileField(upload_to=engagement_date_path)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "attribution": self.attribution,
            "statement": self.statement,
            "alt_text": self.alt_text,
            "upload": self.upload.url,
        }

    def __str__(self):
        return f"Artifact {self.pk} {self.engagement.date.isoformat()}"


class DownloadableFile(models.Model):
    engagement = models.ForeignKey(Engagement, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    upload = models.FileField(upload_to=engagement_date_path)
    is_audio = models.BooleanField("Audio", default=False, help_text="If checked, this file will appear with an audio player on the hub.")
    statement = models.TextField("Connection to Community Resilience Statement", blank=True, help_text="Will appear as a block quote under the image.")
    attribution = models.CharField("Attribution for Statement", max_length=255, blank=True, help_text="Will appear as the attribution for the connection to resilience statement (aka who said the statement).")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "title": self.title,
            "upload": self.upload.url,
            "is_audio": self.is_audio,
            "attribution": self.attribution,
            "statement": self.statement,
        }

    def __str__(self):
        return f"DownloadableFile {self.pk} {self.engagement.date.isoformat()}"


class YoutubeLink(models.Model):
    engagement = models.ForeignKey(Engagement, on_delete=models.PROTECT)
    link = models.URLField()
    statement = models.TextField("Connection to Community Resilience Statement", blank=True, help_text="Will appear as a block quote under the image.")
    attribution = models.CharField("Attribution for Statement", max_length=255, blank=True, help_text="Will appear as the attribution for the connection to resilience statement (aka who said the statement).")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def to_json(self):
        url = urlparse(self.link)

        qs = parse_qs(url.query)
        if "v" in qs:
            yt_id = qs["v"][0]
        else:
            yt_id = url.path[1:]

        return {
            "link": yt_id,
            "attribution": self.attribution,
            "statement": self.statement,
        }

    def __str__(self):
        return f"YoutubeLink {self.pk} {self.engagement.date.isoformat()}"
