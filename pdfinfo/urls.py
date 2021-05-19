from django.urls import path
from . import views

urlpatterns = [
	path('', views.pdflist, name='pdflist'),
	path('pdfinfo/<int:pdf_id>', views.pdfinfo, name='pdfinfo'),
]