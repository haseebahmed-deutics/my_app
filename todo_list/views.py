from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    # return HttpResponse('<h1> home </h1>')
    return render(request,'home.html')

def about(request):
    # return HttpResponse('<h1> about </h1>')
    return render(request,'about.html')

