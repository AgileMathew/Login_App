from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from models import UserDetails
from django.core.urlresolvers import reverse

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        firstname = request.POST.get("firstname", "")
        lastname = request.POST.get("lastname", "")
        mailid = request.POST.get("mailid", "")
        password = request.POST.get("password", "none")
        userdata = User(username=username,first_name=firstname, last_name=lastname, email=mailid)
        userdata.set_password(password)
        userdata.save()
        return HttpResponseRedirect('/login/')
       
    return render(request,"loginapp/register.html")

def signin(request):
    if request.method == "POST":
        print request.POST
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return HttpResponse('welcome')

    return render(request,'loginapp/login.html')
def home(request):

    return render(request, "loginapp/option.html")
