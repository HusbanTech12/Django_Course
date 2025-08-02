from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
 
def home(request):
    return HttpResponse("<h1>Hey I'm a Django Server.</h1>")
    


def about_page(request):
    return HttpResponse('This is a About Page')




