from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from .models import Artifact, Engagement, Place


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
            ])
        formset = ArtifactInlineFormSet(
            instance=self.object
        )

        context["formset"] = formset

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
    fields = (
        "title",
        "description",
        "date",
        "place",
        "comp_equity",
        "comp_community",
        "comp_nature",
        "comp_environment",
        "conn_past",
        "conn_present",
        "conn_future",
    )
    action = "Add"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EngagementUpdateView(LoginRequiredMixin, UpdateView):
    model = Engagement
    fields = (
        "title",
        "description",
        "date",
        "place",
        "comp_equity",
        "comp_community",
        "comp_nature",
        "comp_environment",
        "conn_past",
        "conn_present",
        "conn_future",
    )
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
        formset = ArtifactInlineFormSet(request.POST, request.FILES, instance=engagement)
        if formset.is_valid():
            for form in formset.forms:
                f = form.save(commit=False)
                f.created_by = request.user
                f.save()

            # formset.save()
        else:
            print(formset.errors)

        return redirect(engagement)
