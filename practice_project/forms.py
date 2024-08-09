from django import forms
from django.forms.widgets import NumberInput
import datetime
class PracticeForm(forms.Form):
    name=forms.CharField()
    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email=forms.EmailField()
    agree=forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField( 
    label="Please enter your email address",)
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 