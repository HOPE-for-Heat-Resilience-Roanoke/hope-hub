from django.contrib import admin

from .models import Engagement, Artifact, Place


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
        'comp_equity',
        'comp_community',
        'comp_nature',
        'comp_environment',
        'conn_past',
        'conn_present',
        'conn_future',
    )
    list_filter = (
        'date',
        'comp_equity',
        'comp_community',
        'comp_nature',
        'comp_environment',
        'conn_past',
        'conn_present',
        'conn_future',
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
