from django.forms import ModelForm, DateInput
from .models import Engagement, YoutubeLink

class DateTypeDateInput(DateInput):
    input_type = 'date'

class EngagementForm(ModelForm):
    class Meta:
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

        widgets = {
            "date": DateTypeDateInput(),
        }



class YoutubeLinkForm(ModelForm):
    class Meta:
        model = YoutubeLink
        fields = ["link"]
