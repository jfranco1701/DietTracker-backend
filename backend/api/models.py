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

class Weight(models.Model):
    userid = models.IntegerField(blank=False)
    userweight = models.IntegerField(blank=False)
    weightdate = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.userid) + str(self.userweight)

MEAL_TYPES = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
)

class Food(models.Model):
    name = models.CharField(max_length=100, blank=False)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.name)

class Meal(models.Model):
    userid = models.IntegerField(blank=False)
    mealdate = models.DateField(blank=False)
    mealtype = models.CharField(max_length=10, choices=MEAL_TYPES, blank=False)
    fooditem = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fooditem)
