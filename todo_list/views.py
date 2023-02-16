from django.http import HttpResponse
from django.shortcuts import render
from .models import List
from .forms import Listform
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Listform(request.POST or None)
        if form.is_valid():
            form.save()
            all_list_items = List.objects.all()
            messages.success(request,'Item has been added to List!')
            return render(request, 'home.html', {'active': 'home', 'things': all_list_items})

    else:
        all_list_items = List.objects.all()
        return render(request, 'home.html', {'active': 'home', 'things': all_list_items})


def about(request):
    return render(request, 'about.html', {'active': 'about'})
