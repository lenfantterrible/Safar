from django.shortcuts import redirect
from django.urls import path 
from .views import FlightList


app_name = 'api'


urlpatterns = [
    path('flights/', FlightList.as_view(), name='flight_list'),
    # path('flights/', lambda request : redirect('/'), name='agency_detail'),

]
