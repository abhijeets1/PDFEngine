from django import forms

class PassFileForm(forms.Form):
	password = forms.CharField(required = True, widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password', 'style':'height:3rem;'}))
	
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))