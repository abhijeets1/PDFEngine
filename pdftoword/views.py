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
			location = 'pdftoword'
			timestamp = str(time())
			file = request.FILES["file"]
			filename_b = file.name
			file.name = timestamp + ' ' + file.name
			cfs.handle_uploaded_file(file, location)
			word_file_name = cfs.pdf_to_word(file)
			return render(request, "pdftoword/toword.html",
				{'filename':filename_b, 'word_file_name':word_file_name,}
			)
		else:
			return render(request, "pdftoword/index.html", {'form':form})
	else:
		form = FileForm()
		return render(request, "pdftoword/index.html", {'form':form})