from django.shortcuts import render
from pdfsearch.models import Pdf

# Create your views here.
def pdflist(request):
	pdfs = Pdf.objects.all()
	return render(request, 'pdfinfo/pdflist.html', context={'pdfs':pdfs})

def pdfinfo(request, pdf_id):
	pdf = Pdf.objects.get(pk=pdf_id)
	return render(request, 'pdfinfo/pdfinfo.html', context={'pdf':pdf})