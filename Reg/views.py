from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Student
from .forms import CourseCreateForm,CourseUpdateForm, StudentCreateForm, StudentUpdateForm


# Create your views here.
@login_required
def home(request):
    context = {"user": request.user}
    return render(request, 'Reg/home.html', context)


class ListCourse(LoginRequiredMixin, ListView):
    model = Course

class CreateCourse(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'Reg/course_create_form.html'
    form_class = CourseCreateForm
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
class UpdateCourse(LoginRequiredMixin,UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = 'Reg/course_update_form.html'
class DeleteCourse(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'Reg/course_delete_form.html'
    success_url = '/course/'
    
class ListStudent(LoginRequiredMixin, ListView):
    model = Student 
    
class CreateStudent(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'Reg/student_create_form.html'
    form_class = StudentCreateForm

class UpdateStudent(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'Reg/student_update_form.html'
    form_class = StudentUpdateForm
    
class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'Reg/student_delete_form.html'
    success_url = '/student/'