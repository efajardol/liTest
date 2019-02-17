from DriversVehicles.models import Driver, Vehicle
from DriversVehicles.serializers import DriverSerializer, VehicleSerializer, histSerializer, countSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from django.db.models import Count

class DriversList(generics.ListCreateAPIView):
    queryset=Driver.objects.all()
    serializer_class=DriverSerializer
    
class idDriverDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset=Driver.objects.all()
    serializer_class=DriverSerializer
    lookup_field='driver_id'
    query_pk_and_slug = True

class nameDriverDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset=Driver.objects.all()
    serializer_class=DriverSerializer
    lookup_field='name'
    query_pk_and_slug = True

class vplateDriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Driver.objects.all()
    serializer_class=DriverSerializer
    lookup_field='vehicle__plate'
    query_pk_and_slug = True
      
class VehiclesList(generics.ListAPIView):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer

class histBrandVehiclesList(generics.ListAPIView):
    queryset=Vehicle.objects.all().values('brand').annotate(count=Count('brand'))
    serializer_class=histSerializer

class countVehicles(generics.RetrieveAPIView):
    serializer_class=countSerializer
    def get_object(self):
        return Vehicle.objects.aggregate(count=Count('id'))
