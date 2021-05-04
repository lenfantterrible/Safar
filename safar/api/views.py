from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .permissions import IsAdminOrReadOnly
from .serializers import FlightSerializer
from ticket.models import Flight 


class FlightList(ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer 
    permission_classes = [IsAdminOrReadOnly]
    
    
