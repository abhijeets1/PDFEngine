from core.forms import PdfSearchForm, PageForm, BookForm
from django.http import HttpResponseRedirect
from core import corefunctions as  cfs
from django.shortcuts import render
from .models import Pdf
import pdfplumber
import time

# Create your views here.
def index(request):
	form = PdfSearchForm(auto_id=True)
	return render(request, 'pdfsearch/index.html', context={'form':form})

def pdfsearch(request):
	text_dict = {}
	if request.method == 'POST':
		form = PdfSearchForm(request.POST)
		if form.is_valid():
			search_text = form.cleaned_data['search_bar']
			global_key = form.cleaned_data['global_key']
			for field, value in form.cleaned_data.items():
				if value == True and field != 'global_key':
					pdf_id = int(field[4:])
					text_dict[pdf_id]={}
					text_dict[pdf_id]['pdf_info'] = Pdf.objects.get(pk=pdf_id)
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

	for pdf_id in text_dict.keys():
		pdf = pdfplumber.open('pdfs/' + str(pdf_id) + ".pdf")
		n = len(pdf.pages)
		limit = 10
		page = 0
		while page < (n if n < limit else limit):
			data = str(pdf.pages[page].extract_text())
			for item in search_text_list:
				if (data.find(item) != -1):
					text_dict[pdf_id][page+1] = ' '.join(data.split()[:100]) + '...'
					break
				else:
					if limit < 30:
						limit += 1
			page += 1
		# print(time.asctime(time.localtime(time.time())))
		# while page < n:
		# 	data = str(pdf.pages[page].extract_text())
		# 	for item in search_text_list:
		# 		if (data.find(item) != -1):
		# 			text_dict[pdf_id][page+1] = ' '.join(data.split()[:100]) + '...'
		# 			break
		# 	page += 1
		pdf.close()
		# print(time.asctime(time.localtime(time.time())))

	page_form = PageForm(
		auto_id=False,
		initial={'search_text':search_text, 'global_key':global_key}
	)

	book_form = BookForm(
		auto_id=False,
		initial={'search_text':search_text, 'global_key':global_key, 'limit':10}
	)

	return render(request, 'pdfsearch/pdfsearch.html',
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
			pdf_id = form.cleaned_data['pdf']
			page_no = int(form.cleaned_data['page_no'])

	if global_key == 'True':
		search_text_list = [search_text.capitalize(), search_text.lower(), search_text.upper()]
		if search_text not in search_text_list:
			search_text_list.insert(0, search_text)
	else:
		search_text_list = [search_text]

	pdf = pdfplumber.open('pdfs/' + str(pdf_id) + ".pdf")
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
			pdf_id = form.cleaned_data['pdf']
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
	pdf = pdfplumber.open('pdfs/' + str(pdf_id) + ".pdf")
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
			'pdf':pdf_id,
			'text_dict':text_dict,
			'search_text_list': search_text_list,
			'global_key': global_key,
			'book_form':book_form,
		}
	)