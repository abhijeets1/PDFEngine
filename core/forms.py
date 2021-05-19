from django import forms

class FilesForm(forms.Form):
	files = forms.FileField(widget=forms.ClearableFileInput(
		attrs={'multiple': True, 'class':'form-control'}
	))

	def clean(self):
		for file in self.files.getlist("files"):
			if not (file.content_type == 'application/pdf' and file.size <= 15728640):
				raise forms.ValidationError('')

class FileForm(forms.Form):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))

	def clean(self):
		for file in self.files.getlist("file"):
			if not (file.content_type == 'application/pdf' and file.size <= 15728640):
				raise forms.ValidationError('')

class SplitForm(forms.Form):
	pageno = forms.IntegerField(required = True, widget = forms.NumberInput(
		attrs={'class':'form-control', 'placeholder':'Initial Page Number', 'style':'height:3rem;'}
	))
	
	nofpages = forms.IntegerField(required = True, widget = forms.NumberInput(
		attrs={'class':'form-control', 'placeholder':'Number of Pages', 'style':'height:3rem;'}
	))

	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))

	def clean(self):
		for file in self.files.getlist("file"):
			if not (file.content_type == 'application/pdf' and file.size <= 15728640):
				raise forms.ValidationError('')

class PassFileForm(forms.Form):
	password = forms.CharField(required = True, widget = forms.PasswordInput(
		attrs={'class':'form-control', 'placeholder':'Enter Password', 'style':'height:3rem;'}
	))

	file = forms.FileField(widget=forms.ClearableFileInput(
		attrs={'class':'form-control'}
	))

	def clean(self):
		for file in self.files.getlist("file"):
			if not (file.content_type == 'application/pdf' and file.size <= 15728640):
				raise forms.ValidationError('')

class ImagesForm(forms.Form):
	files = forms.FileField(widget=forms.ClearableFileInput(
		attrs={'multiple': True, 'class':'form-control'}
	))

	def clean(self):
		imageformats = ['image/jpeg', 'image/png', 'image/gif']
		for file in self.files.getlist("files"):
			if not ((file.content_type in imageformats) and (file.size <= 5242880)):
				raise forms.ValidationError('')

class ImageForm(forms.Form):
	file = forms.FileField(widget=forms.ClearableFileInput(
		attrs={'class':'form-control'}
	))

	def clean(self):
		imageformats = ['image/jpeg', 'image/png', 'image/gif']
		for file in self.files.getlist("files"):
			if not ((file.content_type in imageformats) and (file.size <= 5242880)):
				raise forms.ValidationError('')

class CustomSearchForm(forms.Form):
	search_bar = forms.CharField(required=True,widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'Enter Search Query', 'style':'height:3rem;'}
	))

	global_key = forms.BooleanField(required=False, label='Global Key')
	
	files = forms.FileField(
		required=True,
		widget=forms.ClearableFileInput(
			attrs={'multiple': True, 'class':'form-control'}
	))

	def clean(self):
		for file in self.files.getlist("files"):
			if not (file.content_type == 'application/pdf' and file.size <= 15728640):
				raise forms.ValidationError('')

class PageForm(forms.Form):
	pdf = forms.CharField(widget=forms.HiddenInput())
	page_no = forms.CharField(widget=forms.HiddenInput())
	search_text = forms.CharField(required=False, widget=forms.HiddenInput())
	global_key = forms.CharField(required=False, widget=forms.HiddenInput())

class BookForm(forms.Form):
	pdf = forms.CharField(widget=forms.HiddenInput())
	search_text = forms.CharField(widget=forms.HiddenInput())
	global_key = forms.CharField(widget=forms.HiddenInput())
	limit = forms.CharField(widget=forms.HiddenInput())

class PdfSearchForm(forms.Form):
	search_bar = forms.CharField(required=True, widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'Enter Search Query', 'style':'height:3rem;'}
	))

	global_key = forms.BooleanField(required=False, label='Global Key')

	pdf_0 = forms.BooleanField(required=False)
	pdf_1 = forms.BooleanField(required=False)
	pdf_2 = forms.BooleanField(required=False)
	pdf_3 = forms.BooleanField(required=False)
	pdf_4 = forms.BooleanField(required=False)
	pdf_5 = forms.BooleanField(required=False)
	pdf_6 = forms.BooleanField(required=False)
	pdf_7 = forms.BooleanField(required=False)
	pdf_8 = forms.BooleanField(required=False)
	pdf_9 = forms.BooleanField(required=False)
	pdf_10 = forms.BooleanField(required=False)

	def clean(self):
		cleaned_data = super().clean()
		if True not in cleaned_data.values():
			raise forms.ValidationError('')