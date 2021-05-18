from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .permissions import IsAdminOrReadOnly
from .serializers import AgencySerializer, FlightSerializer, TrainSerializer, BusSerializer
from ticket.models import Flight, Train, Bus


class FlightSearch(ListAPIView):
    serializer_class = FlightSerializer 
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, origin, destination, *args, **kwargs):
        self.queryset = Flight.objects.filter(origin=origin, destination=destination)
        return super().get(request, *args, **kwargs)


class FlightList(ListCreateAPIView):
    queryset = Flight.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = FlightSerializer


class TrainList(ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer 
    permission_classes = [IsAdminOrReadOnly]
    
        
class TrainSearch(ListAPIView):
    serializer_class = TrainSerializer 
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, origin, destination, *args, **kwargs):
        self.queryset = Train.objects.filter(origin=origin, destination=destination)
        return super().get(request, *args, **kwargs)

class BusList(ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer 
    permission_classes = [IsAdminOrReadOnly]
    
        
class BusSearch(ListAPIView):
    serializer_class = TrainSerializer 
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, origin, destination, *args, **kwargs):
        self.queryset = Bus.objects.filter(origin=origin, destination=destination)
        return super().get(request, *args, **kwargs)