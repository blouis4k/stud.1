from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model

def home(request):
    return HttpResponse("🎉 Create Studios backend is live and working!")

def setup_view(request):
    try:
        call_command('migrate')
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')
        return HttpResponse("✅ Setup complete. You can now log in at /admin/")
    except Exception as e:
        return HttpResponse(f"❌ Error during setup: {e}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('setup/', setup_view),
]
