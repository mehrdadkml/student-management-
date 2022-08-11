from operator import mod
from turtle import update
from venv import create
from django.db import models

# Create your models here.
class Timestamps(models.Model):
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True