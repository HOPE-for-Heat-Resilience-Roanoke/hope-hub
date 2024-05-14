from django.forms import ModelForm
from .models import YoutubeLink


class YoutubeLinkForm(ModelForm):
    class Meta:
        model = YoutubeLink
        fields = ["link"]
