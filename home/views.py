from django.shortcuts import render
from .models import Product


def home(request):

	# if request.method == 'GET':
	# 	print ('GET method .......')
	# elif request.method == 'POST':
	# 	print ('post method ............')

	list_paper = Product.objects.filter(catagory__startswith='paper')
	list_audio = Product.objects.filter(catagory__startswith='audio')
	context = {'list_paper': list_paper, 'list_audio': list_audio}
	template = "home.html"

	return render (request, template, context)

def result(request):
	context = {}
	template = "itemlist.html"
	return render (request, template, context)

#Test
def addtocart(request, productid):

	product_01 = Product.objects.get(product_id = productid)
	context = {'price' : price, 'author': author}
	template = "home.html"
	return render (request, template, context)

#Test2
def addtocart(request, year):	
	product = Product.objects.get(year = year)
	context = {'price' : product.price, 'author': product.author, 'url': product.url}
	template = "home.html"
	return render (request, template, context)