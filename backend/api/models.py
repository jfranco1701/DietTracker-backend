from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

BREED_SIZES = (
    ('Tiny', 'Tiny'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)

RATING_VALUES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Breed(models.Model):
    name = models.CharField(max_length=100, blank=False)
    size = models.CharField(max_length=6, choices=BREED_SIZES)
    friendliness = models.IntegerField(choices=RATING_VALUES)
    trainability = models.IntegerField(choices=RATING_VALUES)
    sheddingamount = models.IntegerField(choices=RATING_VALUES)
    exerciseneeds = models.IntegerField(choices=RATING_VALUES)

    def __str__(self):
        return str(self.name)
