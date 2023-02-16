from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
            messages.success(request, 'Item has been added to List!')
            return render(request, 'home.html', {'active': 'home', 'things': all_list_items})

    else:
        all_list_items = List.objects.all()
        return render(request, 'home.html', {'active': 'home', 'things': all_list_items})


def about(request):
    return render(request, 'about.html', {'active': 'about'})


def delete(request, id):
    if request.method == 'GET':
        obj = get_object_or_404(List, pk=id)
        obj.delete()
        messages.success(request, 'Item has been deleted from List!')
        all_list_items = List.objects.all()
        return render(request, 'home.html', {'active': 'home', 'things': all_list_items})


def cross_off(request, id):
    if request.method == 'GET':
        obj = get_object_or_404(List, pk=id)
        obj.completed = True
        obj.save()
        messages.success(request, 'Item has been crossed_off successfully!')
        all_list_items = List.objects.all()
        return render(request, 'home.html', {'active': 'home', 'things': all_list_items})


def uncross(request, id):
    if request.method == 'GET':
        obj = get_object_or_404(List, pk=id)
        obj.completed = False
        obj.save()
        messages.success(request, 'Item has been uncrossed successfully!')
        all_list_items = List.objects.all()
        return render(request, 'home.html', {'active': 'home', 'things': all_list_items})
