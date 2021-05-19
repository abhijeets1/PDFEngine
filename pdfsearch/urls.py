from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pdfsearchindex'),
	path('pdfsearch/', views.pdfsearch, name='pdfsearch'),
	path('page/', views.page, name='page'),
	path('book/', views.book, name='book'),
]