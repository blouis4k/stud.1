from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.http import HttpResponse
import traceback

def setup_admin(request):
    try:
        steps = []

        steps.append("Starting setup...")

        call_command('migrate')
        steps.append("Migrations complete.")

        User = get_user_model()
        steps.append("User model retrieved.")

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='info@createstudiosleicester.co.uk',
                password='CreateSecureAdmin2025!'
            )
            steps.append("Superuser created.")
        else:
            steps.append("Superuser already exists.")

        steps.append("Setup complete. You can now log in at /admin/")
        return HttpResponse("<br>".join(steps))

    except Exception:
        return HttpResponse('<pre>' + traceback.format_exc() + '</pre>', status=500)
