from django import forms

class SplitForm(forms.Form):
	pageno = forms.IntegerField(
		required = True,
		label = 'Initial Page Number:',
		help_text = 'Initial page number must be more than zero.',
		widget = forms.NumberInput(
			attrs={'class':'form-control'}
		)
	)
	
	nofpages = forms.IntegerField(
		required = True,
		label = 'Number of Pages:',
		help_text = 'Number of pages must be less than total pages.',
		widget = forms.NumberInput(
			attrs={'class':'form-control'}
		)
	)

	file = forms.FileField(
		required = True,
		label = 'Select PDF:',
		help_text = 'Size limit: 15mb',
		widget=forms.ClearableFileInput(attrs={'class':'form-control'})
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