from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
 
def home(request):
    

 peoples = [
    {'name' : 'Husban' , 'age' : 19},
    {'name' : 'Sarim' , 'age' : 18},
    {'name' : 'Abdul Moiz' , 'age' : 18},
    {'name' : 'Abdullah' , 'age' : 15},
    {'name' : 'Baqir' , 'age' : 17},
 ]

 return render(request , 'index.html' , context = {'peoples' : peoples})


def about(request):
   return render(request , 'about.html')

def contact(request):
   return render(request , 'contact.html')



def about_page(request):
    return HttpResponse('This is a About Page')




