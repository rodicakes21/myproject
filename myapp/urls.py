from django.urls import path
from . import views

urlpatterns = [
    # Students
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/update/<int:pk>/', views.course_update, name='course_update'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),

    # Departments
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/update/<int:pk>/', views.department_update, name='department_update'),
    path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),

    # Schedule
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedules/create/', views.schedule_create, name='schedule_create'),
    path('schedules/update/<int:pk>/', views.schedule_update, name='schedule_update'),
    path('schedules/delete/<int:pk>/', views.schedule_delete, name='schedule_delete'),

    # Tuition
    path('tuitions/', views.tuition_list, name='tuition_list'),
    path('tuitions/create/', views.tuition_create, name='tuition_create'),
    path('tuitions/update/<int:pk>/', views.tuition_update, name='tuition_update'),
    path('tuitions/delete/<int:pk>/', views.tuition_delete, name='tuition_delete'),
]
