from django.db import models

# Create your models here.
class Person(models.Model):
    visitors_in = models.IntegerField(default=0)
    visitors_out = models.IntegerField(default=0)