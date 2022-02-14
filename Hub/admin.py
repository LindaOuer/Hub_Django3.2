from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register([Project, Student, Coach])

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'email'
    )
    fields = (
        ('last_name', 'first_name'),
        'email'
    )


admin.site.register(Student, StudentAdmin)

admin.site.register(Coach)

admin.site.register(Project)