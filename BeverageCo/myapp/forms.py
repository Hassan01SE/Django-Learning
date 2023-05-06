from .models import Drinks

from django import forms


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = '__all__'