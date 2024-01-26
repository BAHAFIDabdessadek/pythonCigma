from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_pages(request):
    return HttpResponse("<h1 style='text-align:center;'>Site De GLASSRI</h1>")