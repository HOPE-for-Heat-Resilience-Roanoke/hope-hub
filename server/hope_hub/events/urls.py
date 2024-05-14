from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path(
        route='create',
        view=views.EngagementCreateView.as_view(),
        name='create'
    ),
    path(
        route='places/create',
        view=views.PlaceCreateView.as_view(),
        name='place_create'
    ),
    path(
        route='places/<int:pk>/update',
        view=views.PlaceUpdateView.as_view(),
        name='place_update'
    ),
    path(
        route='<int:pk>/update',
        view=views.EngagementUpdateView.as_view(),
        name='update'
    ),
    path(
        route='<int:pk>',
        view=views.EngagementDetailView.as_view(),
        name='detail'
    ),
    path(
        route='',
        view=views.EngagementListView.as_view(),
        name='list'
    ),
    path(
        route='<int:pk>/artifacts/create',
        view=views.ArtifactCreateView.as_view(),
        name='artifact_create'
    ),
    path(
        route='<int:pk>/downloadablefiles/create',
        view=views.DownloadableFileCreateView.as_view(),
        name='downloadablefile_create'
    ),
    path(
        route='<int:pk>/youtubelink/create',
        view=views.YoutubeLinkCreateView.as_view(),
        name='youtubelink_create'
    ),
]
