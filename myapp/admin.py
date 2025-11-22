from django.contrib import admin
from .models import Student, Course, Department, Schedule, Tuition

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Schedule)
admin.site.register(Tuition)
