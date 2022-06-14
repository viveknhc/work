from django.shortcuts import render
from exam.models import Question,Exam,Registration
# Create your views here.
def studentHome(request):
    student = Exam.objects.all()
    return render(request,"studenthome.html",{"student":student})
def details(request):
    object1 = Exam.objects.all()
    details = Question.objects.all()
    return render(request,"details.html",{"details":details,"object1":object1})