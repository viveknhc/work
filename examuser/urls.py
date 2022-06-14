from django.urls import path,include

from exam.views import question
from . import views

urlpatterns=[
path('studentHome',views.studentHome,name='studentHome'),
path('details',views.details,name='details'),

]