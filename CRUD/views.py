from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Patients
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.

# def Signup(request):
#     if request.method == 'POST':
#          username = request.POST.get('username')
#          email = request.POST.get('email')
#          password = request.POST.get('password')
#          cpassword = request.POST.get('cpassword')
#          if password != cpassword:
#             messages.error(request, "Passwords does not match")
#             return redirect('/signup')    
#          if User.objects.filter(username=username).exists():
#              messages.error(request, "Username Already Exists")
#              return redirect('/signup')
#          if User.objects.filter(email=email).exists():
#              messages.error(request, "Email Already Exists")
#              return redirect('/signup')
#          myuser = User.objects.create(username = username, email = email, password = password, cpassword = cpassword)
#          myuser.save()
#          messages.success(request,"Successfully Signup Please Login")
#          return redirect("/login")
#     return render(request,'Signup.html')

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect('/signup')    
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('/signup')
        
        # Create the user object without passing cpassword
        myuser = User.objects.create_user(username=username, email=email, password=password)
        
        messages.success(request, "Successfully signed up. Please login.")
        return redirect("/login")
    
    return render(request, 'Signup.html')


def handlelogin(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password = request.POST.get('password')
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Successfully')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
    return render(request,'Login.html')

def INDEX(request):
    pat=Patients.objects.all()
    context = {
        'pat':pat,
    }
    return render(request,'index.html',context)


def ADD(request):
    if request.method == 'POST':
        Patient_ID = request.POST.get('Patient_ID')
        Name = request.POST.get('Name')
        Age = request.POST.get('Age')
        Disease = request.POST.get('Disease')
        Location = request.POST.get('Location')

        pat = Patients(                               #id not used if used it will be updated so id used in update form
            Patient_ID = Patient_ID, Name = Name, Age = Age, Disease = Disease, Location = Location
        )
        pat.save()
        return redirect('home')
    return render(request,'index.html')


def Edit(request):
    pat=Patients.objects.all()

    context = {
        'pat':pat,
    }
    return redirect(request,'index.html',context)


def Update(request,id):  #id used in update form
    if request.method == "POST":
        Patient_ID = request.POST.get('Patient_ID')
        Name = request.POST.get('Name')
        Age = request.POST.get('Age')
        Disease = request.POST.get('Disease')
        Location = request.POST.get('Location')

        pat = Patients(                               
            id = id, Patient_ID = Patient_ID, Name = Name, Age = Age, Disease = Disease, Location = Location
        )
        pat.save()
        return redirect('home')
    return redirect(request,'index.html')


def Delete(request,id):
    pat=Patients.objects.filter(id = id)
    pat.delete()

    context = {
        'pat':pat,
    }
    return redirect('home')
    