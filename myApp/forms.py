from django import forms
from .models import PracticeModel

class practiceModel(forms.ModelForm):
    class Meta:
        model=PracticeModel
        fields='__all__'