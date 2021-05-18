from django.shortcuts import redirect
from django.urls import re_path, path
from .views import FlightList, FlightSearch, TrainList, TrainSearch, BusList, BusSearch


app_name = 'api'


urlpatterns = [
    path(r'flights/', FlightList.as_view(), name='flight_list'),
    re_path(r'^flights/(?P<origin>[a-zA-Z]{1,10})-(?P<destination>[a-zA-Z]{1,10})', FlightSearch.as_view(), name='flight_search'),
    path(r'trains/', TrainList.as_view(), name='train_list'),
    re_path(r'^trains/(?P<origin>[a-zA-Z]{1,10})-(?P<destination>[a-zA-Z]{1,10})', TrainSearch.as_view(), name='train_search'),
    path(r'bus/', BusList.as_view(), name='bus_list'),
    re_path(r'^bus/(?P<origin>[a-zA-Z]{1,10})-(?P<destination>[a-zA-Z]{1,10})', BusSearch.as_view(), name='bus_search'),

]
