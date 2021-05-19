from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pdftowordindex'),
	path('toword/', views.toword, name='toword'),
]