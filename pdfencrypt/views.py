from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from core.forms import PassFileForm
from django.shortcuts import render
from time import time

# Create your views here.
def index(request):
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
			encrpyted_file_name, exceptions = cfs.encrypt_file(file, password, timestamp)
			if len(exceptions) > 0:
				return render(request, "pdfencrypt/index.html",
					{'form':form, 'exceptions': exceptions}
				)
			return render(request, "pdfencrypt/encrypt.html",
				{'filename':filename_b, 'encrpyted_file_name':encrpyted_file_name,}
			)
		else:
			return render(request, "pdfencrypt/index.html", {'form':form})
	else:
		form = PassFileForm()
		return render(request, "pdfencrypt/index.html", {'form':form})