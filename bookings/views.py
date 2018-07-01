from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect

from .models import Booking
from customers.models import Customer
from .forms import BookingForm, CustomerForm

class BookingCreateView(CreateView):
    template_name = 'bookings/booking_add.html'
    model = Booking
    form_class = BookingForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        customer_form = CustomerForm()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  customer_form=customer_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        customer_form = CustomerForm(request.POST)
        customer = None
        # If returning customer
        if customer_form.is_valid():
            customer, _ = Customer.objects.get_or_create(phone_number=customer_form.cleaned_data['phone_number'])
        if form.is_valid() and customer is not None:
            return self.form_valid(form, customer)
        else:
            return self.form_invalid(form, customer_form)

    def form_valid(self, form, customer):
        """
        Called if all forms are valid. Checks for an available cleaner.
        """
        import pdb; pdb.set_trace()
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, customer_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  customer_form=customer_form))
    


class BookingList(ListView):
    model = Booking
