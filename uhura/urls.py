
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

	# add to joins app
	url(r'^$', 'home.views.home', name='home'),

	# url(r'^itemlist$', 'home.views.result', name='home'),
	
	# Test
	# url(r'^addtocart/([0-9][a-z])/$', 'home.views.addtocart'),

	url(r'^addtocart/([0-9]{4})/$', 'home.views.addtocart'),

	url(r'^admin/', include(admin.site.urls)),
	]
