
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def view_static(request):
    return render(request,'temp_static.html')