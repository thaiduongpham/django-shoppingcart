
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

	# add to joins app
	url(r'^$', 'home.views.home', name='home'),

	url(r'^itemlist$', 'home.views.result', name='home'),
	
	url(r'^addtocart$', 'home.cart.add_to_cart'),

	url(r'^admin/', include(admin.site.urls)),
	]
