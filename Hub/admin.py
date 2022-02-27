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

class ProjetDurationListFilter(admin.SimpleListFilter):
    title = 'Duration'
    parameter_name = 'duration'

    def lookups(self, request, model_admin):
        return (
            ('1 month', ("less than a month")),
            ('3 months', ("More than 3 months"))
        )

    def queryset(self, request, queryset):
        if self.value() == '1 month':
            return queryset.filter(project_duration__lte=30)
        if self.value() == '3 months':
            return queryset.filter(project_duration__lte=90, project_duration__gte=30)

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'project_duration',
        'creator',
        'supervisor'
    )
    
    list_filter = (
        'creator',
        'isValid',
        ProjetDurationListFilter,
    )
    
    #date_hierarchy = 'updated_at'
    # radio_fields = {"supervisor": admin.VERTICAL}
    # readonly_fields = ('created_at',)
    
    autocomplete_fields = ['supervisor']

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