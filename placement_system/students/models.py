from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    skills = models.TextField(blank=True)
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.enrollment_number})"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
