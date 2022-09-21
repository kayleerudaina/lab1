from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class WatchlistItem(models.Model):
    watched = models.BooleanField(max_length=255)
    title = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), 
                                             MinValueValidator(1)])
    release_date = models.DateField()
    review = models.TextField()