from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('account/', include('django.contrib.auth.urls'), name="login"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('course/',views.ListCourse.as_view(), name="listcourse"),
    path('course/update/<pk>', views.UpdateCourse.as_view(), name="updatecourse"),
    path('course/delete/<pk>', views.DeleteCourse.as_view(), name="deletecourse"),
    path('course/create', views.CreateCourse.as_view(), name="createcourse"),
    path('student/', views.ListStudent.as_view(), name="liststudent"),
    path('student/create', views.CreateStudent.as_view(), name="createstudent"), 
    path('student/update/<pk>', views.UpdateStudent.as_view(), name="updatestudent"),
    path('student/delete/<pk>', views.DeleteStudent.as_view(), name="deletestudent"),
]
