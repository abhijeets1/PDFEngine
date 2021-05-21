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
	pdf_11 = forms.BooleanField(required=False)
	pdf_12 = forms.BooleanField(required=False)
	pdf_13 = forms.BooleanField(required=False)
	pdf_14 = forms.BooleanField(required=False)
	pdf_15 = forms.BooleanField(required=False)
	pdf_16 = forms.BooleanField(required=False)
	pdf_17 = forms.BooleanField(required=False)
	pdf_18 = forms.BooleanField(required=False)
	pdf_19 = forms.BooleanField(required=False)
	pdf_20 = forms.BooleanField(required=False)
	pdf_21 = forms.BooleanField(required=False)
	pdf_22 = forms.BooleanField(required=False)
	pdf_23 = forms.BooleanField(required=False)
	pdf_24 = forms.BooleanField(required=False)
	pdf_25 = forms.BooleanField(required=False)
	pdf_26 = forms.BooleanField(required=False)
	pdf_27 = forms.BooleanField(required=False)
	pdf_28 = forms.BooleanField(required=False)
	pdf_29 = forms.BooleanField(required=False)
	pdf_30 = forms.BooleanField(required=False)
	pdf_31 = forms.BooleanField(required=False)
	pdf_32 = forms.BooleanField(required=False)
	pdf_33 = forms.BooleanField(required=False)
	pdf_34 = forms.BooleanField(required=False)
	pdf_35 = forms.BooleanField(required=False)
	pdf_36 = forms.BooleanField(required=False)
	pdf_37 = forms.BooleanField(required=False)
	pdf_38 = forms.BooleanField(required=False)
	pdf_39 = forms.BooleanField(required=False)
	pdf_40 = forms.BooleanField(required=False)
	pdf_41 = forms.BooleanField(required=False)
	pdf_42 = forms.BooleanField(required=False)
	pdf_43 = forms.BooleanField(required=False)
	pdf_44 = forms.BooleanField(required=False)
	pdf_45 = forms.BooleanField(required=False)
	pdf_46 = forms.BooleanField(required=False)
	pdf_47 = forms.BooleanField(required=False)

	def clean(self):
		cleaned_data = super().clean()
		pdf_options = {key: value for key, value in cleaned_data.items() if 'pdf_' in key}
		
		if True not in pdf_options.values():
			raise forms.ValidationError('')