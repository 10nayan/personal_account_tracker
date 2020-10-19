from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.conf import settings
# Create your models here.
MY_CHOICES=(('food','food'),('health','health'),('transport','transport'),('utilities','utilities'),('other','other'))
class Report(models.Model):
    description=models.CharField(max_length=30)
    cost=models.IntegerField()
    date=models.DateField()
    tags=MultiSelectField(choices=MY_CHOICES)
    profileLinked=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user')
    def __str__(self):
        return f"{self.description} costs {self.cost} rupees on {str(self.date)}."
    def get_absolute_url(self):
        return reverse ('detail',kwargs={'id':self.id})