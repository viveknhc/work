from ast import Delete
from collections import UserList
import email
from importlib.metadata import requires
from itertools import product
import json
from tkinter import Variable
from urllib import request, response
from django.shortcuts import redirect, render
from .models import Apiusers, Signup,productdetails
from django.views.decorators.http import require_http_methods
from decorator import user_login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serialisers import ApiUserSerializer


# Create your views here.
def wrkfn(request):
    return render(request,"work.html")
def emeafn(req):
    return render(req,"college.html")
def instifn(request):
    return render(request,"institution.html")
def stdzfn(request):
    return render(request,"studentszone.html")
def deptfn(request):
    return render(request,"department.html")
def acadfn(request):
    return render(request,"acadamics.html")
def pfn(request):
    return render(request,"product.html")
def bfn(request):
    return render(request,"baabtra.html")
def cfn(request):
    return render(request,"courses.html")
def confn(request):
    return render(request,"contact.html")
def mfn(request):
    return render(request,"master.html")
def fbfn(request):
    return render(request,"facebook.html")
def abfn(request):
    return render(request,"about.html")
def defn(request):
    # request.session['customerid']=1
    # Del request.session['customerid']
    company={'companyregid':100,"companyname":"apple","country":"us","status":"active"}
    return render(request,"delimiters.html",{"company":company})
def iffn(request):
    userdetails=[{
        "username":"harshin","address":"calicut","number":"123"},
            {
         "username":"sreehari","address":"mlp","number":"9887" },
         {  
            "username":"firas","address":"pkd","number":"1223"
        }]
    return render(request,"jinjaif.html",{"usernameA":"harshin",'response':userdetails})
def formfn(request):
    if request.method=="POST":
        name=request.POST['txt1']
        passwo=request.POST['pass']
        if(name=="harshin" and passwo=="123"):
            return render(request,"college.html")
        else:
            return render(request,"jinjaform.html",{"Errormsg":"failed"})
    return render(request,"jinjaform.html")

    
def tributefn(request):
    return render(request,"tribute.html")


def signupfn(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
        userdetails = Signup(fname=fname,lname=lname,mobile=mobile,email=email,password=password)
        userdetails.save()

        return render(request,"signup.html",{'status':"data inserted successfully..."})
    else:
        return render(request,"signup.html")
def loginfn(request):
    if request.method == 'POST': 
        username=request.POST['username']
        passw=request.POST['passw']
        try:
            logindata = Signup.objects.get(email=username,password=passw)
            request.session['userid']=logindata.id
            print(logindata)
            return redirect('/home')
        except Signup.DoesNotExist:
            return render(request,"login.html",{'error':"invalid user"})
    else:
         return render(request,"login.html")

@user_login_required
def homefn(request):
    if request.method == "POST":
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        Change=Signup.objects.filter(id=request.session['userid']).update(email=email,mobile=mobile)
        return redirect('/home')
    else:
        id=request.session['userid']
        userDetails=Signup.objects.get(id=id)
        return render(request,"home.html",{'name':userDetails})

def deletefn(request):
    id=request.session['userid']
    delete=Signup.objects.filter(id=id).delete()
    delete.request.session['userid']
    return redirect('/login')



def binaryfn(request):
    return render(request,"binary.html")

# decoretor
@require_http_methods(['GET'])
def newfn(request):
    return render(request,'signup.html')

def logoutfn(request):
    del request.session['userid']
    return redirect('/login')

def addprofn(request):
    if request.method == 'POST':
        userid=request.session['userid']
        pname=request.POST['pname']
        quantity=request.POST['quantity']
        pimg=request.FILES['pimg']
        product=productdetails(productName=pname,quantity=quantity,image=pimg,userid_id=userid)
        product.save()
        return render(request, "addpro.html", {'status':1})

    else:
        return render(request, "addpro.html", {'status':0})
def disprofn(request):
    product_data=productdetails.objects.filter(userid_id=request.session['userid'])
    return render(request,'displaypro.html',{'product': product_data})

@api_view(['GET','POST'])   
def apifn(req):
    if req.method == 'POST':
        # data = req.data
        # print(data['username'])
        # user=data['username']
        # passw=data['password']
        # api1=Apiusers(username=user,password=passw)
        # api1.save()
        request = JSONParser().parse(req)
        userSerializer = ApiUserSerializer(data=request)
        if userSerializer.is_valid():
            userSerializer.save()
        else:
            return Response({'status':'Invalid user'})

        return Response({'status':'data inserted'})
    else:  
        user = Apiusers.objects.all()
 #adding a user
        # userlist =[]
        # for i in user:
        #     userlist.append({"username":i.username,"password":i.password})
        #     print(userlist)
        userlist = ApiUserSerializer(user,many=True)
        return Response({'userdetails':userlist.data})
    
# ajax

@csrf_exempt  
def checkfn(request):
    print("success")
    name = request.POST['name']
    obj1 = Signup.objects.filter(fname=name).exists()
    print(obj1)
    print(name)
    return JsonResponse({"isExist":obj1})

def ajaxfn(request):
    return render(request,"ajax.html")

@csrf_exempt 
def adduserfn(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    mobile = request.POST['mobile']
    email = request.POST['email']
    password = request.POST['password']
    user1=Signup(fname=fname,lname=lname,mobile=mobile,email=email,password=password)
    user1.save()
    return JsonResponse({"msg":"data inserted successfully"})

