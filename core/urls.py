from django.http import HttpResponse

def setup_admin(request):
    return HttpResponse("Hello! This route is working.")
