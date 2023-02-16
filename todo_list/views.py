from django.http import HttpResponse
from django.shortcuts import render
from .models import List

# Create your views here.

def home(request):
    all_list_items=List.objects.all()
    return render(request, 'home.html', {'active': 'home','things':all_list_items})


def about(request):
    return render(request, 'about.html', {'active': 'about'})
