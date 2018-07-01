from django.db import models

from customers.models import Customer
from cleaners.models import Cleaner

class Booking(models.Model):
    # By default FKs are required
    customer = models.ForeignKey(Customer)
    cleaner = models.ForeignKey(Cleaner)
    # By default, datetime fields are required
    date = models.DateTimeField()