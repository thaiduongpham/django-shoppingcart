from django.contrib import admin

# Register your models here.
from .models import Product
from .models import CartItem

class ProductAdmin(admin.ModelAdmin):
	
	list_display = ['product_id', 'name', 'author','year', 'price','url','catagory']
	class Meta:
		model = Product

admin.site.register(Product,ProductAdmin)

class CartItemAdmin(admin.ModelAdmin):
	
	list_display = ['id', 'cart_id', 'date_added', 'quantity','product']
	class Meta:
		model = Product

admin.site.register(CartItem,CartItemAdmin)