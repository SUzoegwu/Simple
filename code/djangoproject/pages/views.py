from django.shortcuts import render

def home(request):
	from pages.namer import namer
	return render(request, "home.html", {"introduction": namer})

def about(request):
	return render(request, "about.html", {}) 