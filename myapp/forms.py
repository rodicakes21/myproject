from django import forms
from .models import Student, Course, Department, Schedule, Tuition

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'date_of_birth', 'email']
        widgets = {'date_of_birth': forms.DateInput(attrs={'type': 'date'})}

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'course_code', 'units', 'description']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_id', 'department_name', 'head_of_dept', 'office_loc', 'contact']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['schedule_id', 'course', 'instructor', 'day_of_week', 'time_slot']

class TuitionForm(forms.ModelForm):
    class Meta:
        model = Tuition
        fields = ['payment_id', 'course', 'amount', 'semester', 'due_date']
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}
