from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Name"}))
    dept=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Department"}))
    admission_date=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Admission Date","type":"date"}))
    class Meta:
        model=Student 
        fields='__all__'
        exclude=["created_at","m_id"]
