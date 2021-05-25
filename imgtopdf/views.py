from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from django.shortcuts import render
from core.forms import ImagesForm
from time import time

# Create your views here.
def index(request):
	if request.method == 'POST':
		filenames_b = []
		filenames_a = []
		form = ImagesForm(request.POST, request.FILES)
		if form.is_valid():
			location = 'imgtopdf'
			timestamp = str(time())
			for file in request.FILES.getlist("files"):
				filenames_b.append(file.name)
				file.name = timestamp + ' ' + file.name
				filenames_a.append(file.name)
				cfs.handle_uploaded_file(file, location)
			topdf_file_name = cfs.image_to_pdf(filenames_a, timestamp)
			return render(request, "imgtopdf/topdf.html",
				{'filelist':filenames_b, 'topdf_file_name':topdf_file_name,}
			)
		else:
			return render(request, "imgtopdf/index.html", {'form':form})
	else:
		form = ImagesForm()
		return render(request, "imgtopdf/index.html", {'form':form})