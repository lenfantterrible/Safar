from rest_framework import serializers
from rest_framework.fields import ChoiceField
from rest_framework.relations import RelatedField
from ticket.models import Agency, Flight, Train, Bus


class AgencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agency
        fields = ['logo', 'name']


class AgencyField(serializers.RelatedField):

    def __init__(self, type, *args, **kwargs):
        self.queryset = Agency.objects.filter(type=type)
        super().__init__(*args, **kwargs)
    
    def to_representation(self, value):
        return value.id

    def to_internal_value(self, data):
        return Agency.objects.get(id=data)

class FlightSerializer(serializers.ModelSerializer):
    
    agency = AgencyField('FL')


    class Meta:
        model = Flight
        fields = '__all__'

# class MiddleWayStationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = MiddleWayStation
#         fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):

    agency = AgencyField('TR')


    class Meta:
        model = Train
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):

    agency = AgencyField('BS')

    class Meta:
        model = Bus
        fields = '__all__'

