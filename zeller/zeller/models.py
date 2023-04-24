from django.db import models
from django.contrib.auth.models import User


class AbstractBase(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True
