from rest_framework import serializers
from DriversVehicles.models import Driver, Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields ='__all__'

class DriverSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    class Meta:
        model = Driver
        fields = '__all__'
        #fields= ('driver_id','id_image','name','email_address','vehicle')
        #depth = 1
    def create(self, validated_data):
        vehicle_data = validated_data.pop('vehicle')
        vehicle = Vehicle.objects.create(**vehicle_data)
        return Driver.objects.create(vehicle=vehicle,**validated_data)

        
