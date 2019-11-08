from django.contrib import admin
from .models import Acadamy,Department,Semester,Shift,Subjects,Class_Rooms
# Register your models here.
admin.site.register(Acadamy)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Subjects)
admin.site.register(Class_Rooms)
admin.site.register(Shift)