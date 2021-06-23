from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    temp_name='index.html'
    obj=Crud.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        ins=Crud(name=name,lastname=lastname,password=password)
        messages.success(request,'your data successfuly submited')
        ins.save() 
          
    print(obj)
    return render(request,temp_name,{'obj':obj})
def deletedata(request,id):
    if request.method=="POST":
        ins=Crud.objects.get(pk=id)
        ins.delete()
    return HttpResponseRedirect("/")
def updatedata(request,id):
    if request.method=="POST":
        ins=Crud.objects.get(pk=id)
         
        ins.save()
    ins=Crud.objects.get(pk=id)
    ins.save()
    return render(request,"index.html",{"ins":ins})