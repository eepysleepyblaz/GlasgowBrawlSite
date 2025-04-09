from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):

    context_dict = {}

    return render(request, 'brawl/home.html', context = context_dict)