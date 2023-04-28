from django.db import models
from core_site.models import AbstractBase
from inventory.models import Stock


class Buyer(AbstractBase):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=12, null=False, blank=False)
    address = models.TextField()
    email = models.CharField(max_length=128)
    social_media_handle = models.CharField(max_length=128)


class Sale(AbstractBase):
    class SalesChannel(models.TextChoices):
        Instagram = 'Instagram', 'Instagram'
        Other = 'Other', 'Other'

    product = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    sold_to = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_amount = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sold_on = models.DateTimeField(null=True, blank=True)
    medium = models.CharField(max_length=128, choices=SalesChannel.choices, default=SalesChannel.Instagram)


