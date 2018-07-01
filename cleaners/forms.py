from django import forms

from .models import Cleaner
from cities.models import City

class CleanerForm(forms.ModelForm):
    cities = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Cleaner
        fields = ['first_name', 'last_name', 'quality_score', 'cities']
