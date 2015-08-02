from django.shortcuts import render
from .models import Product
# from orders.cart import test_method

def home(request):

	list_paper = Product.objects.filter(catagory__startswith='paper')
	list_audio = Product.objects.filter(catagory__startswith='audio')

	context = {'list_paper': list_paper, 'list_audio': list_audio}
	template = "home.html"

	return render (request, template, context)