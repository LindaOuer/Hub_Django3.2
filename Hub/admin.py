from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register([Project, Student, Coach])

class ProjectInline(admin.TabularInline):
    model = Project
    fieldsets = [
        (
            None,
            {
                'fields': ['project_name']
            }
        )
    ]
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
    inlines = [
        ProjectInline
    ]
@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'email'
    )
    fields = (
        ('last_name', 'first_name'),
        'email'
    )
    search_fields = ['last_name']

admin.site.register(Student, StudentAdmin)

#admin.site.register(Coach)

admin.site.register(Project)