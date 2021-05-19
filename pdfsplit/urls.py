from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pdfsplitindex'),
	path('split/', views.split, name='split'),
]