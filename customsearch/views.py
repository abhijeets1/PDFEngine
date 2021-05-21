from core.forms import CustomSearchForm, PageForm, BookForm
from django.http import HttpResponseRedirect
from core import corefunctions as cfs
from django.shortcuts import render
from time import time
import pdfplumber

# Create your views here.
pdf_path = 'customsearch/static/upload/'

def index(request):
	form = CustomSearchForm()
	return render(request, "customsearch/index.html", {'form':form})

def customsearch(request):
	if request.method == 'POST':
		text_dict = {}
		filenames_b = []
		filenames_a = []
		form = CustomSearchForm(request.POST, request.FILES)
		if form.is_valid():
			location = 'customsearch'
			timestamp = str(time())
			search_text = form.cleaned_data['search_bar']
			global_key = form.cleaned_data['global_key']
			for file in request.FILES.getlist("files"):
				filenames_b.append(file.name)
				file.name = timestamp + ' ' + file.name
				filenames_a.append(file.name)
				cfs.handle_uploaded_file(file, location)
		else:
			return HttpResponseRedirect('../')
	else:
		return HttpResponseRedirect('../')

	if global_key == 'True':
		search_text_list = [search_text.capitalize(), search_text.lower(), search_text.upper()]
		if search_text not in search_text_list:
			search_text_list.insert(0, search_text)
	else:
		search_text_list = [search_text]

	for filename in filenames_a:
		text_dict[filename] = {}
		pdf = pdfplumber.open(pdf_path + filename)
		n = len(pdf.pages)
		page = 0
		limit = 5
		while page < (n if n < limit else limit):
			data = str(pdf.pages[page].extract_text())
			for item in search_text_list:
				if (data.find(item) != -1):
					text_dict[filename][page+1] = ' '.join(data.split()[:100]) + '...'
					break
				else:
					if limit < 30:
						limit += 1
			page += 1
		pdf.close()
		
	page_form = PageForm(
		auto_id=False,
		initial={'search_text':search_text, 'global_key':global_key}
	)

	book_form = BookForm(
		auto_id=False,
		initial={'search_text':search_text, 'global_key':global_key, 'limit':10}
	)

	return render(request, 'customsearch/customsearch.html',
		context={
			'search_text':search_text,
			'search_text_list':search_text_list,
			'text_dict':text_dict,
			'page_form':page_form,
			'book_form':book_form,
		}
	)

def page(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			search_text = form.cleaned_data['search_text']
			global_key = form.cleaned_data['global_key']
			pdf = form.cleaned_data['pdf']
			page_no = int(form.cleaned_data['page_no'])
		else:
			print('false')

	if global_key == 'True':
		search_text_list = [search_text.capitalize(), search_text.lower(), search_text.upper()]
		if search_text not in search_text_list:
			search_text_list.insert(0, search_text)
	else:
		search_text_list = [search_text]

	pdf_path = 'customsearch/static/upload/'
	pdf = pdfplumber.open('customsearch/static/upload/' + pdf)
	page_text = str(pdf.pages[page_no-1].extract_text())
	pdf.close()

	return render(request, 'core/page.html',
		context={
			'search_text_list':search_text_list,
			'page_no':page_no,
			'page_text':page_text,
		}
	)

def book(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			pdfname = form.cleaned_data['pdf']
			search_text = form.cleaned_data['search_text']
			global_key = form.cleaned_data['global_key']
			limit = int(form.cleaned_data['limit'])
			
	if global_key == 'True':
		search_text_list = [search_text.capitalize(), search_text.lower(), search_text.upper()]
		if search_text not in search_text_list:
			search_text_list.insert(0, search_text)
	else:
		search_text_list = [search_text]

	text_dict = {}
	pdf = pdfplumber.open(pdf_path + pdfname)
	n = len(pdf.pages)
	for page in range(n if n < limit else limit):
		data = str(pdf.pages[page].extract_text())
		text_dict[str((page)+1)] = data
	pdf.close()

	limit += 10
	book_form = BookForm(
		auto_id=False,
		initial={
			'search_text':search_text,
			'global_key':global_key,
			'limit':limit,
		}
	)
	return render(request, 'core/book.html',
		context={
			'pdf':pdfname,
			'text_dict':text_dict,
			'search_text_list': search_text_list,
			'global_key': global_key,
			'book_form':book_form,
		}
	)