from django.forms import ModelForm
from .models import URLShortener

class UrlShortenerForm(ModelForm):
    class Meta:
        model = URLShortener
        fields = ['long_url']