from django.db import models
from django.contrib.auth.models import User


class AbstractBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_created_%(class)s_related")
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name="user_modified_%(class)s_related")

    class Meta:
        abstract = True
