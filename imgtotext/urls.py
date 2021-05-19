from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='imgtotextindex'),
	path('totext/', views.totext, name='totext'),
]