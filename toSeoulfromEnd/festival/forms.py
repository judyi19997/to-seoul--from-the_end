from .models import festival_M
from django import forms

class festival_F(forms.ModelForm):
    period = forms.DateField(
           label='Festival',
           widget=forms.widgets.DateInput(attrs={'type':'date'}),
       )

    class Meta():
        model = festival_M
        fields = ['title','locate','period','body','image','is_school','link']
