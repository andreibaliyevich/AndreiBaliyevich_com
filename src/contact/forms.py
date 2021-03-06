from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """ Message Form """

    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'content',
        ]
