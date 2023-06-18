from django import forms
from .models import Course, Student

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "level")
class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "level")
        
class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name','last_name','gender','age')
        
class StudentUpdateForm(forms.ModelForm):
    class Meta:
         model = Student
         fields = ("first_name","last_name", "gender", "age")
    
        