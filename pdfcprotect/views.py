from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from django.shortcuts import render
from core.forms import FileForm
from time import time

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			location = 'pdfcprotect'
			timestamp = str(time())
			file = request.FILES["file"]
			filename_b = file.name
			file.name = timestamp + ' ' + file.name
			cfs.handle_uploaded_file(file, location)
			cprotected_file_name = cfs.pdf_copy_protect(file.name, timestamp)
			return render(request, "pdfcprotect/cprotect.html",
				{'filename':filename_b, 'timestamp':timestamp, 'cprotected_file_name':cprotected_file_name}
			)
		else:
			return render(request, "pdfcprotect/index.html", {'form':form})
	else:
		form = FileForm()
		return render(request, "pdfcprotect/index.html", {'form':form})