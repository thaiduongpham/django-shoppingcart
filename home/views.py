from django.shortcuts import render
from .models import Product

def home(request):

	list_paper = Product.objects.filter(catagory__startswith='paper')
	list_audio = Product.objects.filter(catagory__startswith='audio')
	context = {'list_paper': list_paper, 'list_audio': list_audio}
	template = "home.html"

	return render (request, template, context)

# def go_to_cart(request):



# 	context = {}
# 	template = "cart.html"
# 	return render (request, template, context)

#Test
def addtocart(request, productid):

	product_01 = Product.objects.get(product_id = productid)
	context = {'price' : price, 'author': author}
	template = "home.html"
	return render (request, template, context)

#Test2
# def addtocart(request, year):	
# 	product = Product.objects.get(year = year)
# 	context = {'price' : product.price, 'author': product.author, 'url': product.url}
# 	template = "home.html"
# 	return render (request, template, context)