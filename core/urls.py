from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.http import HttpResponse
import traceback

def setup_admin(request):
    try:
        call_command('migrate')

        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='info@createstudiosleicester.co.uk',
                password='CreateSecureAdmin2025!'
            )
            return HttpResponse("Superuser created! You can now log in at /admin/")
        return HttpResponse("Admin already exists. You can log in at /admin/")
    except Exception:
        return HttpResponse('<pre>' + traceback.format_exc() + '</pre>', status=500)
