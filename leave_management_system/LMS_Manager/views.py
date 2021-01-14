from django.shortcuts import render
from django.http import HttpResponse
from LMS_Manager.models import *
# Create your views here.

def home(request):
    List_of_holidays = HolidayList.objects.all()

    context = {'HolidayList':List_of_holidays}
    return render(request,'LMS_Manager/home.html', context)

def profile(request):
    return render(request,'LMS_Manager/profile.html')

def leaves(request):
    return render(request,'LMS_Manager/apply_leaves.html')