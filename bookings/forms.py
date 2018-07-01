from django import forms
from django.forms.models import inlineformset_factory

from .models import Booking
from customers.models import Customer
from cities.models import City
from cleaners.models import Cleaner

class BookingForm(forms.ModelForm):
    city = forms.ModelChoiceField(
        queryset=City.objects.all()
    )
    cleaner = forms.ModelChoiceField(
        queryset=Cleaner.objects.all(),
        widget=forms.HiddenInput(),
        required=False)

    class Meta:
        model = Booking
        exclude = ('customer',)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ('id', )
