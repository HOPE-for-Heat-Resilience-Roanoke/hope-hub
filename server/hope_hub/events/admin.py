from django.contrib import admin

from .models import Engagement, Artifact, Place, DownloadableFile, YoutubeLink


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'latitude',
        'longitude',
        'created_by',
        'created',
    )
    list_filter = ('created_by', 'created')
    search_fields = ('name',)


@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'created_by'
    )
    list_filter = (
        'date',
        'created_by'
    )
    ordering = ('-date',)


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'engagement',
        'attribution',
        'upload',
    )


@admin.register(DownloadableFile)
class DownloadableFileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'engagement',
        'title',
        'upload',
        'created_by',
        'created',
        'updated',
    )


@admin.register(YoutubeLink)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'engagement',
        'link',
        'created_by',
        'created',
        'updated',
    )
