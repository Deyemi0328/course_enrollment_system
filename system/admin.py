from django.contrib import admin
from system.models import ForCourse, ForStudent, Enrollment

# Register your models here.
admin.site.register(ForStudent)
admin.site.register(ForCourse)
admin.site.register(Enrollment)
