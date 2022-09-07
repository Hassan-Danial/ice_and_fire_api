from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class book(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=200, null=False)
    isbn = models.CharField(default=False, blank=False,
                            null=False, max_length=25)
    authors = ArrayField(models.CharField(max_length=25), blank=False)
    number_of_pages = models.IntegerField(null=False)
    publisher = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=50, null=False)
    release_date = models.DateTimeField()
    