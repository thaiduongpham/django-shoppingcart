from django.db import models

# Create a Product Model here
class Product(models.Model):
	product_id = models.CharField(max_length=30, primary_key=True)
	name = models.CharField(max_length=30)
	author = models.CharField(max_length=100)	
	year = models.IntegerField()
	price = models.IntegerField(default = 0)
	url = models.CharField(max_length=100, default = '/static/img/audio.jpg')	
	catagory = models.CharField(max_length=30, default = 'no_catagory')

	


