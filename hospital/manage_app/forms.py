from django import forms
from manage_app.models import pationt_list
class admission_form(forms.ModelForm):
    class Meta:
        model=pationt_list
        fields=['name','age','desease','pationt_type']