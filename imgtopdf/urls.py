from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='imgtopdfindex'),
	path('topdf/', views.topdf, name='topdf'),
]