from django import forms
from .models import Card

class CreateForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['question', 'answer']


