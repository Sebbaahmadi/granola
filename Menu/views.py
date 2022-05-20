from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def Granola(request):

    return render(request,'Menu/Granola.html')



def ProteinBites(request):

    return render(request,'Menu/ProteinBites.html')



def Bowls(request):

    return render(request,'Menu/Bowls.html')
