from select import select
from turtle import title
from urllib import request
from django.shortcuts import render,redirect
from exam.models import Exam, Question, Registration

# from examuser.models import Signup

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        name = request.POST['username']
        passwo = request.POST['password']
        if(name == "vivek" and passwo == "vivek123"):
            return render(request,'homepageAdmin.html')
        else:
            loginDetails = Registration.objects.get(username=name,password=passwo)
            request.session['userid']=loginDetails.id
            return redirect('/examuser/studentHome')
    return render(request,"userlogin.html")

def homepageAdmin(request):
    return render(request,"homepageAdmin.html")

def studentRegister(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        stdDetails = Registration(name=name,username=username,password=password)
        stdDetails.save()
        return render(request,"studentRegister.html",{"status":"data inserted successfully"})
    else:
        return render(request,"studentRegister.html",{"status":"not inserted"})

def createExam(request):
    if request.method == 'POST':
        title = request.POST['title']
        subject = Exam(title = title)
        subject.save()
        return redirect("/exam/question")
    return render(request,"createExam.html")

def question(request): 
    object1 = Exam.objects.all()
    if request.method == "POST":
        selection = request.POST['sub']
        questions = request.POST['qstn']
        opt1 = request.POST['opt1']
        opt2 = request.POST['opt2']
        opt3 = request.POST['opt3']
        opt4 = request.POST['opt4']
        mark = request.POST['mark']
        answer = request.POST['answer']
        qst = Question(titles=selection,qstn=questions,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,mark=mark,answer=answer)
        qst.save()
        
    return render(request,"question.html",{"object1":object1})