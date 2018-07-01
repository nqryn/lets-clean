from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import City


class CityList(ListView):
    model = City


class CityDetail(DetailView):
    model = City


class CityCreation(CreateView):
    model = City
    success_url = reverse_lazy('cities:list')
    fields = ['name']


class CityUpdate(UpdateView):
    model = City
    success_url = reverse_lazy('cities:list')
    fields = ['name']


class CityDelete(DeleteView):
    model = City
    success_url = reverse_lazy('cities:list')