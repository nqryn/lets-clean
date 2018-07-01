from django.db import models


class City(models.Model):
    # The name of the city also acts as an unique identifier
    # If need be, we can add state/county/district here
	name = models.CharField(max_length=200, unique=True)

	def __unicode__(self):
		return str(self.name)
