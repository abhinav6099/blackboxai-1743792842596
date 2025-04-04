from django import forms
from .models import Student
from django.core.validators import FileExtensionValidator

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'enrollment_number',
            'department',
            'semester',
            'cgpa',
            'skills',
            'resume',
            'phone_number'
        ]
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3}),
        }
        help_texts = {
            'resume': 'Upload your resume in PDF or Word format',
            'cgpa': 'Enter your current CGPA',
        }

    def clean_enrollment_number(self):
        enrollment_number = self.cleaned_data['enrollment_number']
        if Student.objects.filter(enrollment_number=enrollment_number).exists():
            raise forms.ValidationError("This enrollment number is already registered.")
        return enrollment_number