from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from django.shortcuts import render
from core.forms import FilesForm
from time import time

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = FilesForm(request.POST, request.FILES)
		if form.is_valid():
			filenames_b = []
			filenames_a = []
			location = 'pdfmerge'
			timestamp = str(time())
			for file in request.FILES.getlist("files"):
				filenames_b.append(file.name)
				file.name = timestamp + ' ' + file.name
				filenames_a.append(file.name)
				cfs.handle_uploaded_file(file, location)
			merged_file_name = cfs.merge_files(filenames_a, timestamp)
			return render(request, "pdfmerge/merge.html",
				{'filenames':filenames_b, 'merged_file_name': merged_file_name,}
			)
		else:
			return render(request, "pdfmerge/index.html", {'form':form})
	else:
		form = FilesForm()
		return render(request, "pdfmerge/index.html", {'form':form})