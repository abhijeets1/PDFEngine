from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pdfmergeindex'),
	path('merge/', views.merge, name='merge'),
]