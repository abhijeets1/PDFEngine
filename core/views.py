from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'core/index.html')

def sitedes(request):
	return render(request, 'core/sitedescription.html')

def aboutdevs(request):
	return render(request, 'core/aboutdevelopers.html')