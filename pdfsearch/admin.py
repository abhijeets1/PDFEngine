from django.contrib import admin
from .models import Pdf
# Register your models here.
class PdfsAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'author', 'pages', 'image']

admin.site.register(Pdf, PdfsAdmin)