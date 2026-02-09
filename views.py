from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# READ: List all students and their courses
def student_list(request):
    students = Student.objects.all()
    return render(request, 'enrollment/student_list.html', {'students': students})

# CREATE: Add a new student and enroll them in courses
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'enrollment/student_form.html', {'form': form})

# DELETE: Remove a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'enrollment/student_confirm_delete.html', {'student': student})
