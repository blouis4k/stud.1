from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def setup_admin(request):
    return HttpResponse("Hello! This route is working.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setup/', setup_admin),
]
