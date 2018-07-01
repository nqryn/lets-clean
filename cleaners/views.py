from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Cleaner
from .forms import CleanerForm


class CleanerList(ListView):
    model = Cleaner


class CleanerDetail(DetailView):
    model = Cleaner


class CleanerCreation(CreateView):
    form_class = CleanerForm
    template_name = 'cleaners/cleaner_form.html'
    success_url = reverse_lazy('cleaners:list')


class CleanerUpdate(UpdateView):
    form_class = CleanerForm
    template_name = 'cleaners/cleaner_form.html'
    success_url = reverse_lazy('cleaners:list')
    queryset = Cleaner.objects.all()


class CleanerDelete(DeleteView):
    model = Cleaner
    success_url = reverse_lazy('cleaners:list')