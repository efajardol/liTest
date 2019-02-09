from django.test import TestCase
from django.core.files import File
from ..models import Driver, Vehicle

class DVTest(TestCase):
    def setUp(self):
                
        id_imag1=File(open('DriversVehicles/tests/cedula_frontal.jpg','rb'))
        self.assertEqual(id_imag1.name,'DriversVehicles/tests/cedula_frontal.jpg')
        id_imag2=File(open('DriversVehicles/tests/Cedula_atras2016.jpg','rb'))
        self.assertEqual(id_imag2.name,'DriversVehicles/tests/Cedula_atras2016.jpg')

        Driver.objects.create(
            driver_id=1024123456,
            id_image=id_imag1,
            name='jhon doe',
            email_address='jhondoe@gmail.com',
            vehicle=Vehicle.objects.create(
                plate='asd123',
                vtype='VA',
                brand='KI')
        )
        
        Driver.objects.create(
            driver_id=512123456,
            id_image=id_imag2,
            name='ana doe',
            email_address='anadoe@gmail.com',
            vehicle=Vehicle.objects.create(
                plate='qwe123',
                vtype='SC',
                brand='MZ')
        )
        
    def test_DVget(self):
                
        searchName=Driver.objects.get(name='jhon doe')
        searchID=Driver.objects.get(driver_id=512123456)
        searchPlate=Driver.objects.get(
            vehicle_id=
            ( Vehicle.objects.get(plate='qwe123') ).id
        )
        
        self.assertEqual(searchName.name,'jhon doe')
        self.assertEqual(searchID.driver_id,512123456)
        self.assertEqual(searchPlate.vehicle.plate,'qwe123')

    def test_DVQuery(self):
        regVehicles=Vehicle.objects.all()
        self.assertEqual(len(regVehicles),2)
        self.assertQuerysetEqual(regVehicles,
                                 ['<Vehicle: asd123>','<Vehicle: qwe123>'],
                                 ordered=False)
        regDrivers=Driver.objects.all()
        self.assertEqual(len(regDrivers),2)
        self.assertQuerysetEqual(regDrivers,
                                 ['<Driver: jhon doe>','<Driver: ana doe>'],
                                 ordered=False)
