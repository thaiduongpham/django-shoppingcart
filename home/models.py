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

# Define CartItem in Cart  
class CartItem(models.Model):
	cart_id = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True) 
	quantity = models.IntegerField(default=1)
	product = models.ForeignKey(Product, unique=False) 
	
	class Meta:
		db_table = 'cart_items' 
		ordering = ['date_added'] 
	
	def total(self): 
		return self.quantity * self.product.price
	
	def name(self):
		return self.product.name
	
	def price(self): 
		return self.product.price

	def get_absolute_url(self): 
		return self.product.get_absolute_url()

	def augment_quantity(self, quantity): 
		self.quantity = self.quantity + int(quantity) 
		self.save()




