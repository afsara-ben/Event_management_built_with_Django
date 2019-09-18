from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('review', 'is_favorite', 'behaviour','price_fairness','professionalism','overall')


