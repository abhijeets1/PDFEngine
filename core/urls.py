from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('sd/', views.sitedes, name='sitedes'),
	path('ad/', views.aboutdevs, name='aboutdevs'),
]