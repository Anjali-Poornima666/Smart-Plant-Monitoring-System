from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name='sensors'

urlpatterns = [
    # /sensors/
	url(r'^home/$', views.index , name='index'),
	url(r'^display/$', views.new_disp, name="new_disp"),
	url(r'^display/humidity/$', views.hum, name="humidity"),
	url(r'^display/table/$', views.table, name="table"),
	url(r'^display/waterlevel/$', views.waterl, name="waterlevel"),
	url(r'^display/temperature/$', views.temp, name="temperature"),
	url(r'^display/soilmoisture/$', views.soil, name="soilmoisture"),
	url(r'^display/(?P<temperature>[0-9]+.[0-9]+)/(?P<humidity>[0-9]+.[0-9]+)/(?P<plant1_soilmoisture>[0-9]+.[0-9]+)/(?P<plant2_soilmoisture>[0-9]+.[0-9]+)/(?P<waterlevel>[0-9]+.?[0-9]*)/(?P<r>[0-9]+.?[0-9]*)/',views.Display,name="Display"),

	#For user login/register/logout
	url(r'^login/$',login,{'template_name':'sensors/login.html'}),
	url(r'^logout/$',logout,{'template_name':'sensors/logout.html'}),
	url(r'^register/$',views.register,name="register")

]
