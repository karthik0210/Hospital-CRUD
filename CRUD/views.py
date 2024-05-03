from django.shortcuts import redirect, render
from .models import Patients
# Create your views here.

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
    