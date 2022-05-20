import email
from email import message
from re import sub
from unicodedata import name
import django
from django.http import HttpResponse
from django.shortcuts import render
from . import views 
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'page/Home.html')

def About (request):
    return render(request,'page/About.html')

def cContact (request):
    if request.method=='POST': #collect data from form
        contact=Contact()
        cName=request.POST.get('Name')
        cEmail=request.POST.get('Email')
        cMessage=request.POST.get('Message')
        
        contact.Name=cName
        contact.Email=cEmail
        contact.Message=cMessage

        contact.save()

        return render(request,'page/Thanku.html') 
    else:
        return render(request,'page/Contact.html')       
