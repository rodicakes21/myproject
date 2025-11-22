from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Department, Schedule, Tuition
from .forms import StudentForm, CourseForm, DepartmentForm, ScheduleForm, TuitionForm

# Helper function to reduce repetition
def object_list(request, model, template):
    items = model.objects.all()
    return render(request, template, {'items': items})

def object_create(request, form_class, template, redirect_name):
    form = form_class(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(redirect_name)
    return render(request, template, {'form': form})

def object_update(request, pk, model, form_class, template, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    form = form_class(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(redirect_name)
    return render(request, template, {'form': form})

def object_delete(request, pk, model, template, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_name)
    return render(request, template, {'object': obj})

# Students
def student_list(request):
    return object_list(request, Student, 'myapp/student_list.html')

def student_create(request):
    return object_create(request, StudentForm, 'myapp/student_form.html', 'student_list')

def student_update(request, pk):
    return object_update(request, pk, Student, StudentForm, 'myapp/student_form.html', 'student_list')

def student_delete(request, pk):
    return object_delete(request, pk, Student, 'myapp/student_confirm_delete.html', 'student_list')

# Courses
def course_list(request):
    return object_list(request, Course, 'myapp/course_list.html')

def course_create(request):
    return object_create(request, CourseForm, 'myapp/course_form.html', 'course_list')

def course_update(request, pk):
    return object_update(request, pk, Course, CourseForm, 'myapp/course_form.html', 'course_list')

def course_delete(request, pk):
    return object_delete(request, pk, Course, 'myapp/course_confirm_delete.html', 'course_list')

# Departments
def department_list(request):
    return object_list(request, Department, 'myapp/department_list.html')

def department_create(request):
    return object_create(request, DepartmentForm, 'myapp/department_form.html', 'department_list')

def department_update(request, pk):
    return object_update(request, pk, Department, DepartmentForm, 'myapp/department_form.html', 'department_list')

def department_delete(request, pk):
    return object_delete(request, pk, Department, 'myapp/department_confirm_delete.html', 'department_list')

# Schedule
def schedule_list(request):
    return object_list(request, Schedule, 'myapp/schedule_list.html')

def schedule_create(request):
    return object_create(request, ScheduleForm, 'myapp/schedule_form.html', 'schedule_list')

def schedule_update(request, pk):
    return object_update(request, pk, Schedule, ScheduleForm, 'myapp/schedule_form.html', 'schedule_list')

def schedule_delete(request, pk):
    return object_delete(request, pk, Schedule, 'myapp/schedule_confirm_delete.html', 'schedule_list')

# Tuition
def tuition_list(request):
    return object_list(request, Tuition, 'myapp/tuition_list.html')

def tuition_create(request):
    return object_create(request, TuitionForm, 'myapp/tuition_form.html', 'tuition_list')

def tuition_update(request, pk):
    return object_update(request, pk, Tuition, TuitionForm, 'myapp/tuition_form.html', 'tuition_list')

def tuition_delete(request, pk):
    return object_delete(request, pk, Tuition, 'myapp/tuition_confirm_delete.html', 'tuition_list')
