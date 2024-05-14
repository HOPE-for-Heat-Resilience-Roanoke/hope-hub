from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from .models import Artifact, Engagement, Place, DownloadableFile, YoutubeLink
from .forms import EngagementForm, YoutubeLinkForm


class EngagementListView(LoginRequiredMixin, ListView):
    model = Engagement

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name="admin").exists():
            context["other_objects"] = self.model.objects.filter(~Q(created_by=self.request.user))

        return context


class EngagementDetailView(LoginRequiredMixin, DetailView):
    model = Engagement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ArtifactInlineFormSet = inlineformset_factory(
            Engagement,
            Artifact,
            fields=[
                "upload",
                "alt_text",
                "statement",
                "attribution",
            ],
            extra=1
        )
        artifact_formset = ArtifactInlineFormSet(
            instance=self.object
        )

        DownloadableFileInlineFormSet = inlineformset_factory(
            Engagement,
            DownloadableFile,
            fields=[
                "upload",
                "title",
            ],
            extra=1
        )
        downloadablefile_formset = DownloadableFileInlineFormSet(
            instance=self.object,
        )

        yl = YoutubeLink.objects.filter(engagement = self.get_object()).first()
        youtubelink_form = YoutubeLinkForm(instance=yl)

        context["artifact_formset"] = artifact_formset
        context["downloadablefile_formset"] = downloadablefile_formset
        context["youtubelink_form"] = youtubelink_form

        return context


class PlaceCreateView(LoginRequiredMixin, CreateView):
    model = Place
    fields = (
        "name",
        "latitude",
        "longitude"
    )
    action = "Add"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["GOOGLE_PLACES_API_KEY"] = settings.GOOGLE_PLACES_API_KEY
        return context

    def get_success_url(self):
        return reverse("events:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PlaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Place
    fields = (
        "name",
        "latitude",
        "longitude"
    )
    action = "Update"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["GOOGLE_PLACES_API_KEY"] = settings.GOOGLE_PLACES_API_KEY
        return context

    def get_success_url(self):
        return reverse("events:list")


class EngagementCreateView(LoginRequiredMixin, CreateView):
    model = Engagement
    form_class = EngagementForm
    action = "Add"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EngagementUpdateView(LoginRequiredMixin, UpdateView):
    model = Engagement
    form_class = EngagementForm
    action = "Update"


class ArtifactCreateView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Engagement

    def post(self, request, *args, **kwargs):
        engagement = self.get_object()

        ArtifactInlineFormSet = inlineformset_factory(
            Engagement,
            Artifact,
            fields=[
                "attribution",
                "statement",
                "alt_text",
                "upload",
            ])
        formset = ArtifactInlineFormSet(
            request.POST,
            request.FILES,
            instance=engagement
        )

        if formset.is_valid():
            for form in formset.forms:
                if form.cleaned_data != {}:
                    f = form.save(commit=False)
                    f.created_by = request.user
                    f.save()
        else:
            print(formset.errors)

        return redirect(engagement)


class DownloadableFileCreateView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Engagement

    def post(self, request, *args, **kwargs):
        engagement = self.get_object()

        DownloadableFileInlineFormSet = inlineformset_factory(
            Engagement,
            DownloadableFile,
            fields=[
                "upload",
                "title",
            ])
        downloadablefile_formset = DownloadableFileInlineFormSet(
            request.POST,
            request.FILES,
            instance=engagement
        )

        if downloadablefile_formset.is_valid():
            for form in downloadablefile_formset.forms:
                if form.cleaned_data != {}:
                    f = form.save(commit=False)
                    f.created_by = request.user
                    f.save()
        else:
            print(downloadablefile_formset.errors)

        return redirect(engagement)


class YoutubeLinkCreateView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Engagement

    def post(self, request, *args, **kwargs):
        engagement = self.get_object()

        youtubelink_form = YoutubeLinkForm(request.POST)
        if youtubelink_form.is_valid():
            f = youtubelink_form.save(commit=False)

            f.engagement = engagement
            f.created_by = request.user

            f.save()
        else:
            print(youtubelink_form.errors)

        return redirect(engagement)
