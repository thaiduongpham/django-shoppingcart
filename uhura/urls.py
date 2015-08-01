
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

	# add to joins app
	url(r'^$', 'home.views.home', name='home'),

	url(r'^showcart$', 'orders.cart.go_to_cart'),
	
	url(r'^addtocart$', 'orders.cart.add_to_cart'),

	url(r'^sendemail$', 'orders.cart.send_email'),

	url(r'^admin/', include(admin.site.urls)),
	]
