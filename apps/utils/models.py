from operator import mod
from turtle import update
from venv import create
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Timestamps(models.Model):
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.DO_NOTHING,
                                   related_name='+')
    modified_by = models.ForeignKey(get_user_model(),
                                    on_delete=models.DO_NOTHING,
                                    related_name='+')


    class Meta:
        abstract=True