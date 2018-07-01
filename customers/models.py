from django.db import models

class Customer(models.Model):
    # By default, charfields are required
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Phone number is required because it will be used as identification for users
    # We don't make it unique because it will fail validations
    phone_number = models.CharField(max_length=50)
