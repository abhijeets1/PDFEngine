from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='pdfdecryptindex'),
	path('decrypt/', views.decrypt, name='decrypt'),
]