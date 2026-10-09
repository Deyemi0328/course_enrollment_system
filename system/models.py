from django.db import models

# Create your models here.
class ForStudent(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registered_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Firstname
    
class ForCourse(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_duration = models.IntegerField()
    course_instructor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    student = models.ForeignKey(ForStudent, on_delete=models.CASCADE)
    course = models.ForeignKey(ForCourse, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.Firstname} enrolled in {self.course.course_name}"
 