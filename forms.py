from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    # This allows students to select multiple courses from a checklist or menu
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Student
        fields = ['name', 'courses']