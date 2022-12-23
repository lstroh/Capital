from django.db import models

# Create your models here.
class Capital(models.Model):
    country = models.CharField(max_length=100, primary_key=True)
    capital = models.CharField(max_length=100)
    id = models.IntegerField()

