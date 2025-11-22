from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from myapp.models import Student, Enrollment, Schedule, Tuition
from django.db import transaction

# Register new student
def student_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        student_id = request.POST['student_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['date_of_birth']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            error = "Username already exists"
            return render(request, 'online_enrollment/register.html', {'error': error})

        with transaction.atomic():
            user = User.objects.create_user(username=username, password=password)
            Student.objects.create(
                user=user,
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=dob,
                email=email
            )
        return redirect('student_login')
    return render(request, 'online_enrollment/register.html')


# Login
def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_profile')
        else:
            error = "Invalid username or password"
            return render(request, 'online_enrollment/login.html', {'error': error})
    return render(request, 'online_enrollment/login.html')


# Logout
def student_logout(request):
    logout(request)
    return redirect('student_login')


# Profile/dashboard
@login_required
def student_profile(request):
    student = Student.objects.get(user=request.user)
    
    # Courses enrolled by the student
    enrollments = student.enrollment_set.select_related('course')
    courses = [e.course for e in enrollments]
    
    # Schedules for these courses
    schedules = Schedule.objects.filter(course__in=courses)
    
    # Tuition for these courses
    tuitions = Tuition.objects.filter(course__in=courses)
    
    return render(request, 'online_enrollment/profile.html', {
        'student': student,
        'courses': courses,
        'schedules': schedules,
        'tuitions': tuitions,
    })
