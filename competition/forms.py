from django import forms
from . import models

class CreateCompetition(forms.ModelForm):
    class Meta:
        model = models.Competition
        fields = ['name','date']