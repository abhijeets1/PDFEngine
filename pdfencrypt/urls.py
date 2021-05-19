from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pdfencryptindex'),
	path('encrypt/', views.encrypt, name='encrypt'),
]