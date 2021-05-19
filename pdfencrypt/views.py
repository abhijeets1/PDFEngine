from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from core.forms import PassFileForm
from django.shortcuts import render
from time import time

# Create your views here.
def index(request):
	form = PassFileForm()
	return render(request, "pdfencrypt/index.html", {'form':form})

def encrypt(request):
	if request.method == 'POST':
		form = PassFileForm(request.POST, request.FILES)
		if form.is_valid():
			location = 'pdfencrypt'
			timestamp = str(time())
			file = request.FILES["file"]
			password = form.cleaned_data['password']
			filename_b = file.name
			file.name = timestamp + ' ' + file.name

			cfs.handle_uploaded_file(file, location)
			encrpyted_file_name = cfs.encrypt_file(file, password, timestamp)
			if encrpyted_file_name == True:
				return HttpResponseRedirect('../')
			return render(request, "pdfencrypt/encrypt.html",
				{'filename':filename_b, 'encrpyted_file_name':encrpyted_file_name,}
			)
		else:
			return HttpResponseRedirect('../')
	else:
		return HttpResponseRedirect('../')