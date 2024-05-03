from django.contrib import admin

from .models import Engagement, Artifact


@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'place',
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
        'attribution',
        'engagement',
        'upload',
    )
    list_filter = ('engagement',)
