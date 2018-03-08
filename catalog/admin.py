from django.contrib import admin

# Register your models here.
from .models import Teacher, Specialyties, Student, StudentInformation

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Specialyties)
admin.site.register(StudentInformation)