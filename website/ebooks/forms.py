from django import forms

class UploadForm(forms.Form):
	file = forms.FileField( label='Choose a File to upload', help_text='' )
