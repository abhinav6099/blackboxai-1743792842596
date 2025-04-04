from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'user', 'department', 'semester', 'cgpa')
    search_fields = ('enrollment_number', 'user__first_name', 'user__last_name')
    list_filter = ('department', 'semester')
    ordering = ('enrollment_number',)
