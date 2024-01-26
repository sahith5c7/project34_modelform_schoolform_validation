from django.shortcuts import render

from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sl=SFDO.cleaned_data['Slocation']
            sp=SFDO.cleaned_data['Sprincipal']
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['Reentermail']
            SO=School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp,email=e,Reentermail=re)[0]
            SO.save()
            return HttpResponse('School is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'create_school.html',context=d)
