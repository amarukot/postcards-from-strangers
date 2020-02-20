from django import forms
from .models import Postcard, Sender

class PostcardForm(forms.ModelForm):
    class Meta:
        model = Postcard
        fields = ('image_url', 'heading', 'message',)

