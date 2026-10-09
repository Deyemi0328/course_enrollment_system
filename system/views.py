from django.shortcuts import render, redirect, get_object_or_404
from system.forms import ForStudentForm, ForCourseForm, EnrollmentForm
from .models import ForStudent, ForCourse, Enrollment   
    # Create your views here.
def  StudentReg(request):
        if request.method == 'POST':
            form = ForStudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("display_student")
        else:
                form = ForStudentForm()
        return render(request, 'student.html', {'form':form})

def CourseReg(request):
        if request.method == 'POST':
            form = ForCourseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("display_course")
        else:
                form = ForCourseForm()
        return render(request, 'course.html', {'form': form})

def EnrollmentReg(request):
        message = ''
        if request.method =='POST':
            form = EnrollmentForm(request.POST)
            if form.is_valid():
                    student = form.cleaned_data["student"]
                    course = form.cleaned_data["course"]
                    already_enrolled = Enrollment.objects.filter(
                            student=student, course=course).exists()
                    if already_enrolled:
                            message = "This student is already enrolled in this course."
                    else:
                            form.save()
                            return redirect('display_enrollment')
        else:
                form = EnrollmentForm()
        return render(request, 'enrollment.html', {'form':form, 'message': message})

def display_student(request):
        students = ForStudent.objects.all()
        return render(request, 'display_student.html', {'students': students})

def update_student(request, pk):
        student = ForStudent.objects.get(id=pk)
        if request.method == 'POST':
                form = ForStudentForm(request.POST, instance=student)
                if form.is_valid():
                        form.save()
                        return redirect('display_student')
        else:
                form = ForStudentForm(instance=student)
        return render(request, 'student.html', {'form': form})

def delete_student(request, pk):
        student = ForStudent.objects.get(id=pk)
        if request.method == 'POST':
                student.delete()
                return redirect('display_student')
        return render(request, 'student.html', {'student': student})

def display_course(request):
        courses = ForCourse.objects.all()
        return render(request, 'display_course.html', {'courses': courses})
    
def display_enrollment(request):
        enrollments = Enrollment.objects.all()
        return render(request, 'display_enrollment.html', {'enrollments': enrollments})


def student_info(request, id):
    student = get_object_or_404(ForStudent, id=id)

    enrollments = Enrollment.objects.filter(student=student)

    return render(request, 'student_info.html', {
        'student': student,
        'enrollments': enrollments,
    })

def course_info(request, id):
    course = get_object_or_404(ForCourse, id=id)

    enrollments = Enrollment.objects.filter(course=course)

    return render(request, 'course_info.html', {
        'course': course,
        'enrollments': enrollments,
    })

