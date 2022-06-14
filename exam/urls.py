from django.urls import path,include
from . import views

urlpatterns=[
path('userlogin',views.userlogin,name='userlogin'),
path('homepageAdmin',views.homepageAdmin,name='homepageAdmin'),
path('studentRegister',views.studentRegister,name='studentRegister'),
path('createExam',views.createExam,name='createExam'),
path('question',views.question,name='question'),
]