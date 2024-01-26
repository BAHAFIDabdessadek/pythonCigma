
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pages/", include('pages.urls'), name="pages_application"),
    path("", views.index_project, name="index_project"),
]
