from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Hi, I am coming from firstapp/index.html'}
    return (render(request,'firstapp/index.html', context= my_dict))
