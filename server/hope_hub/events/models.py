from django.conf import settings
from django.db import models
from django.urls import reverse


class Place(models.Model):
    name = models.CharField(max_length=255)

    latitude = models.FloatField()
    longitude = models.FloatField()

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Engagement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    place = models.ForeignKey(Place, on_delete=models.PROTECT)

    comp_equity = models.BooleanField("Comp Plan Equity", default=False, help_text="Interwoven Equity")
    comp_community = models.BooleanField("Comp Plan Community", default=False, help_text="Healthy Community")
    comp_nature = models.BooleanField("Comp Plan Nature", default=False, help_text="Harmony with Nature")
    comp_environment = models.BooleanField("Comp Plan Environment", default=False, help_text="Livable Built Environment")

    conn_past = models.BooleanField("Connection Past", default=False, help_text="Processing the Past")
    conn_present = models.BooleanField("Connection Present", default=False, help_text="Understanding the Present")
    conn_future = models.BooleanField("Connection Future", default=False, help_text="Visioning the Future")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date",)

    def to_json(self):
        return {
            "title": self.title,
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
    alt_text = models.CharField("Image Caption", max_length=255, blank=True, help_text="Caption for the image, also used as the alt text.")
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

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "title": self.title,
            "upload": self.upload.url,
        }

    def __str__(self):
        return f"DownloadableFile {self.pk} {self.engagement.date.isoformat()}"


class YoutubeLink(models.Model):
    engagement = models.ForeignKey(Engagement, on_delete=models.PROTECT)
    link = models.URLField()

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "link": self.link,
        }

    def __str__(self):
        return f"YoutubeLink {self.pk} {self.engagement.date.isoformat()}"
