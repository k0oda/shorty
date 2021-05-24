from django.forms import ModelForm, TextInput
from .models import Link


class ShortenForm(ModelForm):
    class Meta:
        model = Link
        fields = ['original_url',]
        widgets = {
            'original_url': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your URL',
            })
        }
