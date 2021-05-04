from rest_framework import serializers
from ticket.models import Flight 


class FlightSerializer(serializers.ModelSerializer):
    
    # agency = serializers.HyperlinkedIdentityField(view_name='agency_detail')

    class Meta:
        model = Flight
        fields = '__all__'