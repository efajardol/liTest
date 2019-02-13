from django.test import TestCase
from django.core.files import File
from DriversVehicles.models import Driver, Vehicle
from DriversVehicles.serializers import DriverSerializer, VehicleSerializer
from collections import OrderedDict

class DVSerializerTest(TestCase):
    def setUp(self):
        id_imag1=File(open('DriversVehicles/tests/cedula_frontal.jpg','rb'))
        self.assertEqual(id_imag1.name,'DriversVehicles/tests/cedula_frontal.jpg')
        self.data=OrderedDict(
            [('vehicle',
              OrderedDict([('plate', 'qwe123'),
                           ('vtype', 'SC'),
                           ('brand', 'MZ')])),
             ('driver_id', 512123456),
             ('id_image', id_imag1),
             ('name', 'ana doe'),
             ('email_address', 'anadoe@gmail.com')]
        )
        self.vehicle=OrderedDict([
            ('plate', 'qwe123'),
            ('vtype', 'SC'),
            ('brand', 'MZ')]
        )
        self.driver=OrderedDict([
            ('driver_id', 512123456),
            ('name', 'ana doe'),
            ('email_address', 'anadoe@gmail.com')]
        )
         
    def test_ParserRender(self):
        serializer=DriverSerializer(data=self.data)
        serializer.is_valid()
        serializer.save()

        d1 = Driver.objects.get(name='ana doe')
        serializer = DriverSerializer(d1)
        data=serializer.data
        vehicle=data.pop('vehicle')
        vehicle.pop('id')
        self.assertEqual(vehicle,self.vehicle)
        data.pop('id')
        data.pop('id_image')
        self.assertEqual(data,self.driver)
