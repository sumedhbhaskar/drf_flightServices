from ast import Pass
import re
from rest_framework import serializers
from .models import Flight,Passenger,Reservation


def isFlightNumberValid(data):
    print("isFlightValid")

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValid]

    def validate_flightNumber(self,flightNumber):
        if (re.match("^[a-zA-Z0-9]",flightNumber)==None):
            raise serializers.ValidationError("Invalid FlightNumber. Make sure that it is alpha numeric")
        return flightNumber
    
    def validate(self,data):
        print(data['flightNumber'])



class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):

    # flight = FlightSerializer()
    # passenger = PassengerSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'

