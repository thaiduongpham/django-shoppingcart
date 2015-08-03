
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

	url(r'^$', 'home.views.home', name='home'),

	url(r'^showcart$', 'orders.cart.go_to_cart'),
	
	url(r'^addtocart$', 'orders.cart.add_to_cart'),

	url(r'^gettotalproducts$', 'orders.cart.get_total_products'),
	
	url(r'^sendemail$', 'orders.cart.send_email'),

	url(r'^download$', 'orders.cart.donwload_file'),

	url(r'^admin/', include(admin.site.urls)),
	]
