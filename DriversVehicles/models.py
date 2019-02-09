from django.db import models
#from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.   
class Vehicle(models.Model):
    plate = models.CharField('Plate', max_length=6, unique=True)
    VTYPES = (
        ('VA','van'),
        ('PU','pickup'),
        ('TB','turbo'),
        ('SC','sencillo'),
        ('DT','dobletroque'),
        ('CM','cuatromanos'),
        ('MM','minimula'),
        ('T2','tm2troques'),
        ('T3','tm3troques')
    )
    vtype = models.CharField(max_length=2, choices=VTYPES)
    BRANDS = (
        ('VW','Voltswagen'),
        ('CV','Chevrolet'),
        ('RN','Renault'),
        ('KI','Kia'),
        ('FD','Ford'),
        ('MZ','Mazda'),
        ('NS','Nissan'),
        ('SK','Susuki'),
        ('HD','Hyundai')
    )
    brand = models.CharField(max_length=2, choices=BRANDS)
    def __str__(self):
        return self.plate

class Driver(models.Model):
    driver_id = models.PositiveIntegerField('Driver ID', unique=True)
    id_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    name = models.CharField('Name',max_length=100)
    email_address = models.EmailField('Email Address', unique=True)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    #authentication
    def __str__(self):
        return self.name
