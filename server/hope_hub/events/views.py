from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from .models import Artifact, Engagement


class EngagementListView(ListView):
    model = Engagement


class EngagementDetailView(DetailView):
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


class EngagementCreateView(CreateView):
    model = Engagement
    fields = (
        "title",
        "description",
        "date",
        "relevant_location",
        "latitude",
        "longitude",
        "comp_equity",
        "comp_community",
        "comp_nature",
        "comp_environment",
        "conn_past",
        "conn_present",
        "conn_future",
    )


class EngagementUpdateView(UpdateView):
    model = Engagement
    fields = (
        "title",
        "description",
        "date",
        "relevant_location",
        "latitude",
        "longitude",
        "comp_equity",
        "comp_community",
        "comp_nature",
        "comp_environment",
        "conn_past",
        "conn_present",
        "conn_future",
    )
    action = "Update"


class ArtifactCreateView(CreateView):
    model = Artifact
    fields = (
        "upload",
        # "alt_text",
        # "statement",
        # "attribution",
    )

class ArtifactCreateView(SingleObjectMixin, View):
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
        print("anything in request. files".format(request.FILES))
        formset = ArtifactInlineFormSet(request.POST, request.FILES, instance=engagement)
        if formset.is_valid():
            formset.save()
        else:
            print(formset.errors)

        return redirect(engagement)
