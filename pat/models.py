from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.conf import settings
# Create your models here.
MY_CHOICES=(('food','food'),('health','health'),('transport','transport'),('utilities','utilities'),('other','other'))
#model Report is created to store user information with different fields
class Report(models.Model):
    description=models.CharField(max_length=30)
    cost=models.IntegerField()
    date=models.DateField()
    #third party module multiselectfield is used to select many tag fieds at single time
    tags=MultiSelectField(choices=MY_CHOICES)
    #Report model is linked to User model with one to many relationship
    profileLinked=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user')
    #this method returns string representation of an object
    def __str__(self):
        return f"{self.description} costs {self.cost} rupees on {str(self.date)}."
    #this method is used to redirects to a instance's detail view
    def get_absolute_url(self):
        return reverse ('detail',kwargs={'pk':self.pk})