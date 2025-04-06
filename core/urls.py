from django.contrib import admin
from django.urls import path
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.management import call_command
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

    except Exception as e:
        error_message = traceback.format_exc()
        return HttpResponse(f"Error during setup:<br><pre>{error_message}</pre>", status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setup/', setup_admin),
]
