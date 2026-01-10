from django import forms
from .models import Box

class BoxCreateForm(forms.ModelForm):

    class Meta:
        model = Box
        fields = ['name', 'capacity', 'state']


