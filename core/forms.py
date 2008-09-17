from django import forms

class FilesForm(forms.Form):
	files = forms.FileField(
		required = True,
		label = 'Select PDFs:',
		help_text = 'Size limit: 15mb',
		widget=forms.ClearableFileInput(
			attrs={'multiple': True, 'class':'form-control'}
		)
	)

	def clean(self):
		exceptions = []

		for file in self.files.getlist("files"):
			if not (file.content_type == 'application/pdf'):
				exceptions.append('Selected file is not a PDF!')
			if not (file.size <= 15728640):
				exceptions.append('Selected file size is more than 15mb!')

		if len(exceptions) > 0:
			raise forms.ValidationError(exceptions)

class FileForm(forms.Form):
	file = forms.FileField(
		required = True,
		label = 'Select PDF:',
		help_text = 'Size limit: 15mb',
		widget=forms.ClearableFileInput(
			attrs={'class':'form-control'}
		),
	)

	def clean(self):
		exceptions = []

		for file in self.files.getlist("file"):
			if not (file.content_type == 'application/pdf'):
				exceptions.append('Selected file is not a PDF!')
			if not (file.size <= 15728640):
				exceptions.append('Selected file size is more than 15mb!')

		if len(exceptions) > 0:
			raise forms.ValidationError(exceptions)

class PassFileForm(forms.Form):
	password = forms.CharField(
		required = True,
		label = 'Password:',
		widget = forms.PasswordInput(
			attrs={'class':'form-control'}
		),
	)

	file = forms.FileField(
		required = True,
		label = 'Select PDF:',
		help_text = 'Size limit: 15mb',
		widget=forms.ClearableFileInput(
			attrs={'class':'form-control', 'autocomplete':'on'}
		),
	)

	def clean(self):
		exceptions = []

		for file in self.files.getlist("file"):
			if not (file.content_type == 'application/pdf'):
				exceptions.append('Selected file is not a PDF!')
			if not (file.size <= 15728640):
				exceptions.append('Selected file size is more than 15mb!')

		if len(exceptions) > 0:
			raise forms.ValidationError(exceptions)

class ImagesForm(forms.Form):
	files = forms.FileField(
		required = True,
		label = 'Select Images:',
		help_text = 'Size limit: 5mb',
		widget=forms.ClearableFileInput(
			attrs={'multiple': True, 'class':'form-control'}
		)
	)

	def clean(self):
		imageformats = ['image/jpg', 'image/jpeg', 'image/png', 'image/gif']
		exceptions = []

		for file in self.files.getlist("files"):
			if not (file.content_type in imageformats):
				exceptions.append('Selected file is not an image!')
			if not (file.size <= 5242880):
				exceptions.append('Selected file size is more than 5mb!')

		if len(exceptions) > 0:
			raise forms.ValidationError(exceptions)

class ImageForm(forms.Form):
	file = forms.FileField(
		required = True,
		label = 'Select Image:',
		help_text = 'Size limit: 5mb',
		widget=forms.ClearableFileInput(
			attrs={'class':'form-control'}
		)
	)

	def clean(self):
		imageformats = ['image/jpg', 'image/jpeg', 'image/png', 'image/gif']
		exceptions = []

		for file in self.files.getlist("file"):
			if not (file.content_type in imageformats):
				exceptions.append('Selected file is not an image!')
			if not (file.size <= 5242880):
				exceptions.append('Selected file size is more than 5mb!')

		if len(exceptions) > 0:
			raise forms.ValidationError(exceptions)

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