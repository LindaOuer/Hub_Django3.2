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

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'project_duration',
        'creator',
        'supervisor'
    )

    fieldsets = (
        (
            'Etat',
            {
                'fields': ('isValid',)
            }
        ),
        (
            'A Propos',
            {
                'classes': ('collapse',),
                'fields': (
                    'project_name',
                    (
                        'creator',
                        'supervisor',
                    ),
                    'needs',
                    'description',
                ),
            }
        ),
        (
            'Durées',
            {
                'fields': (
                    (
                        'project_duration',
                        'time_allocated'
                    ),
                )
            }
        ),
    )
    
    empty_value_display = '-empty-'

admin.site.register(Student, StudentAdmin)

#admin.site.register(Coach)
admin.site.register(MembershipInProject)

admin.site.register(Project, ProjectAdmin)