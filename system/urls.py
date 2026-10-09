from django.urls import path
from . import views

urlpatterns = [
    path("", views.StudentReg, name="StudentReg"),
    path("register_course/", views.CourseReg, name="CourseReg"),
    path("register_enrollment/", views.EnrollmentReg, name="EnrollmentReg"),
    path("display_students/", views.display_student, name="display_student"),
    path('students/<int:id>/', views.student_info, name='student_info'),
    path("display_courses/", views.display_course, name="display_course"),
    path('courses/<int:id>/', views.course_info, name='course_info'),
    path("display_enrollments/", views.display_enrollment, name="display_enrollment"),
    path('student/<int:pk>/update/', views.update_student, name='update_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete'),
]