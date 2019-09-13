from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('image_name', 'image_file', 'uploader', 'date_added', )

