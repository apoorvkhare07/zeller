from django.db import models
from django.contrib.auth.models import User

# from zeller.core_site.models import AbstractBase

# from json_field import JSONField


class Seller(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    contact = models.CharField(max_length=12, null=False, blank=False)
    address = models.TextField()
    city = models.CharField(max_length=128)
    note = models.TextField()


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512)
    acquired_on = models.DateTimeField(null=False, blank=False)
    buying_price = models.DecimalField(max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    acquired_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='stock_acquired')
    acquiring_cost = models.DecimalField(max_digits=6, decimal_places=2)
    paid_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='stock_paid_for')
    seller = models.ForeignKey(Seller, null=True, blank=True,  on_delete=models.SET_NULL)
    # specifications = JSONField(default={'name': ""})
