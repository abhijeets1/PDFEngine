from django.http import HttpResponseRedirect
from django.shortcuts import render
from core import corefunctions as cfs
from core.forms import SplitForm
from time import time

# Create your views here.
def index(request):
	form = SplitForm()
	return render(request, "pdfsplit/index.html", {'form':form})

def split(request):
	if request.method == 'POST':
		form = SplitForm(request.POST, request.FILES)
		if form.is_valid():
			location = 'pdfsplit'
			timestamp = str(time())
			file = request.FILES["file"]
			pageno = form.cleaned_data['pageno']
			nofpages = form.cleaned_data['nofpages']
			filename_b = file.name
			file.name = timestamp + ' ' + file.name
			cfs.handle_uploaded_file(file, location)
			if cfs.validate_pdf_split(file, pageno, nofpages):
				return HttpResponseRedirect('../')
			splited_file_name = cfs.split_file(file, pageno, nofpages, timestamp)
			return render(request, "pdfsplit/split.html",
				{'filename':filename_b, 'splited_file_name':splited_file_name,}
			)
		else:
			return HttpResponseRedirect('../')
	else:
		return HttpResponseRedirect('../')