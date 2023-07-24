from django import forms
from .models import StuModel,DeptModel

class DeptForm(forms.ModelForm):
	class Meta:
		model = DeptModel
		fields= "__all__"

class StuForm(forms.ModelForm):
	class Meta:
		model = StuModel
		fields= "__all__"




