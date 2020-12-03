from django.db import models

# Create your models here.

class Unknown(models.Model):
	outageid = models.IntegerField()
	shutid = models.IntegerField()
	element = models.CharField(max_length = 50)
	elementid=models.IntegerField(default=1)
	startdate = models.DateField()
	enddate = models.DateField()
	availed = models.BooleanField(null=True) 

class Pwc(models.Model):
	outageid = models.IntegerField(null=True)
	shutid = models.IntegerField()
	element = models.CharField(max_length = 50)
	elementid=models.IntegerField()
	startdate = models.DateField()
	enddate = models.DateField()
	availed = models.BooleanField(null=True)

