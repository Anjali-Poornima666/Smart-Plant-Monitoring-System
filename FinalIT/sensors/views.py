"""# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here."""

from django.shortcuts import render,get_object_or_404,redirect
from .models import Sensors
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sensors.forms import RegistrationForm
from datetime import datetime

#redirecting to main/home page
def index(request):
	return render(request,'sensors/index.html/',{'user':request.user})

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/sensors/login/')
	else:
		form = RegistrationForm()
	return render(request,'sensors/reg_form.html',{'form':form})

#sending last 10 sensor values to respected pages
def hum(request):
	all_sensors = Sensors.objects.all()[Sensors.objects.count()-10:Sensors.objects.count()]
	return render(request ,'sensors/hum.html',{'all_sensors':all_sensors,'user':request.user})

def table(request):
	all_sensors = Sensors.objects.all()[Sensors.objects.count()-10:Sensors.objects.count()][::-1]
	return render(request ,'sensors/table.html',{'all_sensors':all_sensors,'user':request.user})

def temp(request):
	all_sensors = Sensors.objects.all()[Sensors.objects.count()-10:Sensors.objects.count()]
	return render(request ,'sensors/temp.html',{'all_sensors':all_sensors,'user':request.user})

def waterl(request):
	all_sensors = Sensors.objects.all()[Sensors.objects.count()-10:Sensors.objects.count()]
	return render(request ,'sensors/waterl.html',{'all_sensors':all_sensors,'user':request.user})

def soil(request):
	all_sensors = Sensors.objects.all()[Sensors.objects.count()-10:Sensors.objects.count()]
	return render(request ,'sensors/soil.html',{'all_sensors':all_sensors,'user':request.user})

#values obtained from url are stored in database
def Display(request,temperature=None,humidity=None,plant1_soilmoisture=None,plant2_soilmoisture=None,waterlevel=None,r=None):
    all_sensors = Sensors()
    all_sensors.temperature=float(temperature)
    all_sensors.humidity=float(humidity)
    all_sensors.plant1_soilmoisture=float(plant1_soilmoisture)
    all_sensors.plant2_soilmoisture=float(plant2_soilmoisture)
    all_sensors.waterlevel=float(waterlevel)
    if all_sensors.plant1_soilmoisture<20.0 and float(r)<100.0:
        all_sensors.plant1_actuatorstate="ON( PLANT-1 NEEDS WATER !)"
    else:
        all_sensors.plant1_actuatorstate="OFF(PLANT-1 DOESN'T NEED WATER !)"

    if all_sensors.plant2_soilmoisture<20.0 and float(r)<100.0:
        all_sensors.plant2_actuatorstate="ON( PLANT-2 NEEDS WATER !)"
    else:
        all_sensors.plant2_actuatorstate="OFF(PLANT-2 DOESN'T NEED WATER !)"
    if float(r)>100.0:
        all_sensors.rainfall="RAINING"
    else:
        all_sensors.rainfall="NOT RAINING"
    all_sensors.dateAndTime=str(datetime.now()).split('.')[0]
    all_sensors.save()
    return render(request ,'sensors/template/index.html',{'all_sensors':all_sensors,'user':request.user})

#sending latest sensor data to template
def new_disp(request):
    all_sensors = Sensors.objects.get(pk=Sensors.objects.count())
    return render(request ,'sensors/template/index.html',{'all_sensors':all_sensors,'user':request.user})


