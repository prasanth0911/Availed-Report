from django.db import models

# Create your models here.

class Unknown(models.Model):

	outageid = models.IntegerField()
	shutid = models.IntegerField()
	element = models.CharField(max_length = 50)
	startdate = models.DateField()
	enddate = models.DateField()
	availed = models.BooleanField() 


class Planned(models.Model):
	shutid = models.IntegerField()
	element=models.CharField(max_length = 50)
	startdate = models.DateField()
	enddate = models.DateField()