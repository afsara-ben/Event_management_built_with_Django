from django import forms
from .models import event_request, event_message


class requestForm(forms.ModelForm):
    class Meta:
        model = event_request
        fields = ('service', 'range', 'location', 'language', 'goal', 'job', 'size', 'otherservice',
                  'client_remote_work', 'request_status', 'client_name', )


class messageForm(forms.ModelForm):
    class Meta:
        model = event_message
        fields = ('email_subject', 'email_content', )


class servicerequestForm(forms.ModelForm):
    class Meta:
        model = event_request
        fields = ('otherservice', 'service', 'range', 'location', 'language', 'goal', 'job', 'size',
                  'client_remote_work', 'request_status', 'client_name', )

