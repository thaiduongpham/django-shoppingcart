from django.shortcuts import render

# function home process the requests
def home(request):
	context = {}
	template = "home.html"
	return render (request, template, context)

