from django import forms
from track.models import Track
from .models import *

class NewTrainee(forms.Form):
    name = forms.CharField(
        required=True, 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Trainee Name'
        })
    )
    image = forms.ImageField(
        required=False, 
        label='Upload Trainee Image',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Trainee Email'
        })
    )
    age = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Trainee Age'
        })
    )
    phone = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Trainee Phone',
        })
    )
    track = forms.ChoiceField(
        choices=Track.getall(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

class NewtraineeModel(forms.ModelForm):
    track = forms.ChoiceField(choices=Track.getall())
    class Meta:
        model = Trainee
        fields='__all__'
        exclude=['trackobj']
   