from django.shortcuts import render

def home(request):
	context = {}
	template = "home.html"
	return render (request, template, context)


def result(request):
	context = {}
	template = "itemlist.html"
	return render (request, template, context)