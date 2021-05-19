from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from django.shortcuts import render
from core.forms import FileForm
from time import time

# Create your views here.
def index(request):
	ptwf = FileForm()
	return render(request, "pdftoword/index.html", {'form':ptwf})

def toword(request):
	if request.method == 'POST':
		ef = FileForm(request.POST, request.FILES)
		if ef.is_valid():
			location = 'pdftoword'
			timestamp = str(time())
			file = request.FILES["file"]
			filename_b = file.name
			file.name = timestamp + ' ' + file.name
			cfs.handle_uploaded_file(file, location)
			word_file_name = cfs.pdf_to_word(file)
		else:
			return HttpResponseRedirect('../')
		return render(request, "pdftoword/toword.html", {'filename':filename_b, 'word_file_name':word_file_name,})
	else:
			return HttpResponseRedirect('../')