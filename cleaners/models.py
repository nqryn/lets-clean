from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from cities.models import City

class Cleaner(models.Model):
    # By default, charfields are required
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Required, must be a number between 0.0 and 5.0
    quality_score = models.DecimalField(max_digits=2, decimal_places=1, \
    	validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    # The cities in which a cleaner works
    # If more information is needed per city (e.g. quality score or schedule), `through` can be used
    cities = models.ManyToManyField(City, related_name='cleaners')

    def __unicode__(self):
    	return '%s, %s' %(self.last_name, self.first_name)
    