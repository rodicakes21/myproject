from django.db import models
from django.contrib.auth.models import User

# Student model linked to Django User
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

# Course
class Course(models.Model):
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    units = models.CharField(max_length=5)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name

# Department
class Department(models.Model):
    department_id = models.CharField(max_length=20)
    department_name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    office_loc = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name

# Schedule
class Schedule(models.Model):
    schedule_id = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20)
    time_slot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.schedule_id} - {self.course.course_name}"

# Tuition
class Tuition(models.Model):
    payment_id = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    semester = models.CharField(max_length=20)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.payment_id} - {self.course.course_name}"

# Enrollment (link students to courses)
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.course.course_name}"
