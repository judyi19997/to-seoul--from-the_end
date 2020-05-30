from django import forms
from .models import Review

class Reviewform(forms.ModelForm):
    fest_date = forms.DateField(
           label='Festival',
           widget=forms.widgets.DateInput(attrs={'type':'date'}),
       )

    class Meta:
        model = Review
        fields = ['title','body','image','fest_date']