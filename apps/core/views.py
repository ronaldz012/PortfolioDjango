from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.
def test(request):
   return render(request, 'core/index.html')
def home(request):
   return HttpResponse("This is home page")
def about(request):
   return HttpResponse("This is about page")
def contact(request):
   return HttpResponse("This is contact page")
def projects(request):
   return HttpResponse("This is projects page")