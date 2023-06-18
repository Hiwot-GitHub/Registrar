from django.db import models

# Create your models here.
class Course(models.Model):
   
    BEGINNER = "BEG"
    INTERMIDIATE = "MID"
    ADVANCED = "EXP"
    COURSE_LEVEL_CHOICES = [
        ( BEGINNER, "Beginner"),
        (INTERMIDIATE, "Intermidiate"),
        (ADVANCED, "Advanced"),
    ]
    
    level = models.CharField(max_length=3, choices=COURSE_LEVEL_CHOICES, default=BEGINNER)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.title + " "+ self.level
    def get_absolute_url(self):
        return '/course'
    
class Student(models.Model):
    GENDER_CHOICES = [
        ("Female", "Female"),
        ("Male", "Male"),
        ("Other", "Other"),
    ]
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    
    def takes(self):
        course_title = models.ForeignKey(Course, on_delete=models.CASCADE)
        date = models.DateField(auto_now=True)
        
        
    def get_absolute_url(self):
        return '/student'
    
    def __str__(self):
        return self.first_name +" "+ self.last_name