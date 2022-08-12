import email
from django.db import models

from apps.utils.models import Timestamps

class WaitListEntry(Timestamps,models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    notes=models.TextField()