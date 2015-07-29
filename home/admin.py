from django.contrib import admin

# Register your models here.
from .models import Product

# from django.contrib.auth.models import *
# admin.site.unregister(Product) 

class ProductAdmin(admin.ModelAdmin):
	
	list_display = ['product_id', 'name', 'author','year', 'price','url','catagory']
	class Meta:
		model = Product

admin.site.register(Product,ProductAdmin)

# admin.site.register(Product)