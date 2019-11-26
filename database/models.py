from django.db import models

class Suppliers(models.Model):
	
	supplier_id = models.AutoField(primary_key=True)
	company_name = models.CharField(max_length=50)
	contact_name = models.CharField(max_length=50)
	contact_title = models.CharField(max_length=40)
	city = models.CharField(max_length=50)
	region = models.CharField(max_length=40)	
	country = models.CharField(max_length=20)

class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=50)
	description = models.TextField()
	picture = models.BinaryField()

class Products(models.Model):
	product_id = models.AutoField(primary_key=True)
	supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
	caregory_id = models.ForeignKey(Category, on_delete=models.CASCADE)
	quantity_per_unit = models.CharField(max_length=50)
	unit_price = models.DecimalField(max_digits=19, decimal_places=4)
	units_in_stock = models.SmallIntegerField()
	units_on_order = models.SmallIntegerField()
	reorder_level = models.SmallIntegerField()

class Region(models.Model):
	region_id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=50)
	region_description = models.TextField()

