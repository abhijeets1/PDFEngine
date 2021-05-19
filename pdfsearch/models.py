from django.db import models

# Create your models here.
class Pdf(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pages = models.IntegerField()
	image = models.CharField(max_length=100, default="null")