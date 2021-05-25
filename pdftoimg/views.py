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
			location = 'pdftoimg'
			timestamp = str(time())
			file = request.FILES["file"]
			filename_b = file.name
			file.name = timestamp + ' ' + file.name
			cfs.handle_uploaded_file(file, location)
			imagesname = cfs.pdf_to_image(file, timestamp)
			return render(request, "pdftoimg/toimg.html",
				{'filename':filename_b, 'timestamp':timestamp, 'imagesname':imagesname,}
			)
		else:
			return render(request, "pdftoimg/index.html", {'form':form})
	else:
		form = FileForm()
		return render(request, "pdftoimg/index.html", {'form':form})