from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={
            'student_name':'Name of Student',
            'student_marks':'Marks'
        }