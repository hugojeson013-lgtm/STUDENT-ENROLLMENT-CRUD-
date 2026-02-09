from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    # One teacher per course
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    # A student can take many courses
    courses = models.ManyToManyField(Course) 

    def __str__(self):
        return self.name # Create your models here.
