from django.core.files import File
from DriversVehicles.models import Driver, Vehicle

id_imag1=File(open('DriversVehicles/tests/cedula_frontal.jpg','rb'))
id_imag2=File(open('DriversVehicles/tests/Cedula_atras2016.jpg','rb'))

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

#searchName=Driver.objects.get(name='jhon doe')
