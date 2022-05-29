


from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

import flightApp
from flightApp.views import FlightViewsets,ReservationViewsets,PassengerViewsets,find_flight,save_reservation


router = routers.DefaultRouter()
router.register('flight',FlightViewsets)
router.register('passenger',PassengerViewsets)
router.register('reservation',ReservationViewsets)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('find_flight',find_flight),
    path('save_reservation',save_reservation.as_view()),
    path('authtoken',obtain_auth_token,name="api_auth_token")

]
