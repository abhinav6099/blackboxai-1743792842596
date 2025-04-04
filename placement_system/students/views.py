from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import StudentProfileForm

@login_required
def student_dashboard(request):
    try:
        student = request.user.student
    except Student.DoesNotExist:
        return redirect('complete_profile')
    
    context = {
        'student': student
    }
    return render(request, 'students/dashboard.html', context)

@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            messages.success(request, 'Profile completed successfully!')
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm()
    
    return render(request, 'students/complete_profile.html', {'form': form})
