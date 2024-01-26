
from django.http import HttpResponse


def index_project(request):
    return HttpResponse("<h1 style='text-align:center;'>Bienvenue au site LP GLAASRI</h1>")