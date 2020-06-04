from django import forms
from .models import Review

class Reviewform(forms.ModelForm):
    fest_date = forms.DateField(
           label='Festival',
           widget=forms.widgets.DateInput(attrs={'type':'date'}),
       )
    
    # image = forms.ImageField(
    #        label='image',
    #        widget=forms.widgets.FileInput(attrs={'type':'file'}),
    #    )

    class Meta:
        model = Review
        fields = ['title','fest_date','body','image']
