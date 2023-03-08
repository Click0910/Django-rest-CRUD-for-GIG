from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=100)
    bird = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Locations(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    coordinates = models.TextField(blank=True)
    dealer = models.ManyToManyField(Dealer)
