# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Sensors,UserProfile

admin.site.register(Sensors)
admin.site.register(UserProfile)
# Register your models here.

