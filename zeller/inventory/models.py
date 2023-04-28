from django.db import models
from django.contrib.auth.models import User

from core_site.models import AbstractBase

# from json_field import JSONField


class Seller(AbstractBase):
    name = models.CharField(max_length=255, null=False, blank=False)
    contact = models.CharField(max_length=12, null=False, blank=False)
    address = models.TextField()
    city = models.CharField(max_length=128)
    note = models.TextField()


class Camera(AbstractBase):
    class CameraType(models.TextChoices):
        PointAndShoot = 'PointAndShoot', 'PnS'
        RangeFinder = 'RangeFinder', 'RangeFinder'
        SLR = 'SLR', 'slr'

    class Company(models.TextChoices):
        Yashica = 'Yashica', 'Yashica'
        Pentax = 'Pentax', 'Pentax'
        Nikon = 'Nikon', 'Nikon'
        Canon = 'Canon', 'Canon'
        Samsung = 'Samsung', 'Samsung'

    type = models.CharField(max_length=64, choices=CameraType.choices)
    lens = models.CharField(max_length=255)
    battery_type = models.CharField(max_length=255)
    company = models.CharField(max_length=64, choices=Company.choices)


class Film(AbstractBase):
    class FilmType(models.TextChoices):
        Coloured = 'Coloured', 'Coloured'
        BlackAndWhite = 'BlackAndWhite', 'BlackAndWhite'

    class Company(models.TextChoices):
        Samsung = 'Samsung', 'Samsung'
        Kodak = 'Kodak', 'Kodak'
        Ilford = 'Ilford', 'Ilford'

    type = models.CharField(max_length=64, choices=FilmType.choices)
    expiry_year = models.DateTimeField(null=True, blank=True)
    company = models.CharField(max_length=64, choices=Company.choices)
    iso = models.IntegerField(null=True, blank=True)
    exposures = models.IntegerField(null=True, blank=True)


class Stock(AbstractBase):
    title = models.CharField(max_length=512)
    acquired_on = models.DateTimeField(null=False, blank=False)
    buying_price = models.DecimalField(max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    acquired_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='stock_acquired')
    acquiring_cost = models.DecimalField(max_digits=6, decimal_places=2)
    paid_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='stock_paid_for')
    seller = models.ForeignKey(Seller, null=True, blank=True,  on_delete=models.SET_NULL)
    # specifications = JSONField(default={})

