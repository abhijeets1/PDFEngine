from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from django.shortcuts import render
from core.forms import ImageForm
from time import time

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			location = 'imgtotext'
			file = request.FILES["file"]
			timestamp = str(time())
			filename_b = file.name
			file.name = timestamp + ' ' + file.name
			filenameafter = file.name
			cfs.handle_uploaded_file(file, location)
			text, text_file_name = cfs.img_to_text(file, timestamp)
			return render(request, "imgtotext/totext.html",
				{'filename':filename_b, 'text':text, 'text_file_name':text_file_name,}
			)
		else:
			return render(request, "imgtotext/index.html", {'form':form})
	else:
		form = ImageForm()
		return render(request, "imgtotext/index.html", {'form':form})