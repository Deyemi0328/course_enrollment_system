from django import forms
from .models import ForStudent, ForCourse, Enrollment

class ForStudentForm(forms.ModelForm):
    class Meta:
        model = ForStudent
        fields = ['Firstname', 'Lastname', 'email', 'phone_number']

class ForCourseForm(forms.ModelForm):
    class Meta:
        model = ForCourse
        fields = ['course_name', 'course_description', 'course_duration', 'course_instructor']  

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']