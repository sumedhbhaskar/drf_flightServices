from django.shortcuts import render
from rest_framework import viewsets
from .models import Flight,Reservation,Passenger
from .serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class FlightViewsets(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)


class PassengerViewsets(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewsets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# @api_view(['POST'])
# def find_flight(request):
#     flight_qs = Flight.objects.all()
#     filterset = FlightFilter(request.GET,queryset=flight_qs)
#     # if filterset.is_valid():
#     queryset = filterset.qs
#     serializer = FlightSerializer(queryset,many = True)
#     return Response(serializer.data)

@api_view(['POST'])
def find_flight(request):
    flight_qs = Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],estimatedTimeOfDeparture=request.data['estimatedTimeOfDeparture'])
    serializer = FlightSerializer(flight_qs,many=True)
    return Response(serializer.data)

class save_reservation(APIView):
    def post(self,request):
        flight = Flight.objects.get(id=request.data['flightId'])

        passenger = Passenger()
        passenger.firstName = request.data['firstName']
        passenger.lastName = request.data['lastName']
        passenger.middleName = request.data['middleName']
        passenger.email = request.data['email']
        passenger.phone = request.data['phone']
        passenger.save()

        reservation = Reservation()
        reservation.flight = flight
        reservation.passenger = passenger
        reservation.save()

        return Response(status=status.HTTP_201_CREATED)

    