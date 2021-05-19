from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='customsearchindex'),
	path('customsearch/', views.customsearch, name='customsearch'),
	path('page/', views.page, name='cspage'),
	path('book/', views.book, name='csbook'),
]