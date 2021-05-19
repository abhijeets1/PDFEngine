from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pdftoimgindex'),
	path('toimg/', views.toimg, name='toimg'),
]