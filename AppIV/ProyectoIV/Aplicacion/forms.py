from django import forms 

from Aplicacion.models import Enterprise, Calification

class create_enterprise_form(forms.ModelForm):
	class Meta:
		model=Enterprise
		fields=('name','town','sector')

class create_calification_form(forms.ModelForm):
	class Meta:
		model=Calification
		fields=('player','calification','enterprise')
