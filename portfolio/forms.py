from django import forms
from .models import Portfolio

class NewPortfolio(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ('title', 'description', 'image')
