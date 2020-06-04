from .models import festival_M
from django import forms

class festival_F(forms.ModelForm):
    class Meta():
        model = festival_M
        fields = ['title','locate','period','body','image','is_school','link']
