from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.conf import settings
import os


def home(request):
    return HttpResponse("🎉 Create Studios backend is live and working!")


def setup_admin(request):
    try:
        call_command('migrate')  # Run DB migrations
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        return HttpResponse("✅ Setup complete. You can now log in at /admin/")
    except Exception as e:
        return HttpResponse(f"❌ Error during setup:<br><pre>{e}</pre>")


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('setup/', setup_admin),
]
