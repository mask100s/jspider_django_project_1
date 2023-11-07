from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sendresp1(request):
  return HttpResponse("hello you did successfull url mapping 1")

def sendresp2(request):
  return HttpResponse("<h1><marquee>hello you did successfull url mapping 2</marquee></h1>")