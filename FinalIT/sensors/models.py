# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#sensors
class Sensors(models.Model):
	temperature = models.FloatField(default=0)
	humidity = models.FloatField(default=0)
	plant1_soilmoisture=models.FloatField(default=0)
	plant1_actuatorstate=models.CharField(max_length=50)
	plant2_soilmoisture=models.FloatField(default=0)
	plant2_actuatorstate=models.CharField(max_length=50)
	waterlevel=models.FloatField(default=0)
	rainfall=models.CharField(max_length=50)
	dateAndTime=models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

#creates new account
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

