from django.db import models

class Suppliers(models.Model):
	
	CompanyName = models.CharField(max_length=200)
	ContactName = models.CharField(max_length=200)
	ContactTitle = models.CharField(max_length=20)
	City = models.CharField(max_length=100)
	Region = models.CharField(max_length=200)	
	Country = models.CharField(max_length=20)


