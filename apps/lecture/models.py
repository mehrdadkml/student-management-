from django.db import models
from apps.utils.models import Timestamps
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Lecture(Timestamps,models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    Lecture_name=models.CharField(max_length=100,default='',blank=True)
    date=models.DateField()
    slide_url=models.CharField(max_length=255)
    duration=models.IntegerField(default=1,validators=[MaxValueValidator(100),MinValueValidator(1)],help_text='زمان مورد نیاز سخنرانی به ساعت')
    is_required=models.BooleanField(default=True)
